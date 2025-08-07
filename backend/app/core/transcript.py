from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import uuid


@dataclass
class Word:
    text: str
    start_timestamp: float
    end_timestamp: Optional[float] = None


@dataclass
class TranscriptSegment:
    participant_id: str
    participant_name: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    words: List[Word] = field(default_factory=list)
    is_partial: bool = False
    timestamp: datetime = field(default_factory=datetime.now)


class TranscriptStore:
    MERGE_THRESHOLD_SECONDS = 2.0  # Maximum gap between segments to consider merging
    
    def __init__(self):
        self.segments: List[TranscriptSegment] = []
        self.active_partials: Dict[str, str] = {}  # {participant_id: segment_id}
    
    def add_transcript_from_webhook(self, payload: dict) -> Optional[Tuple[str, TranscriptSegment, Optional[str]]]:
        """
        Processes a transcript webhook payload (partial or final) and updates the store.

        Returns:
            A tuple of (action, segment, deleted_segment_id) or None.
            - action: "APPEND", "UPDATE", "FINALIZE", "MERGE_UPDATE"
            - segment: The primary TranscriptSegment that was affected.
            - deleted_segment_id: The ID of a segment that was consumed by a merge.
        """
        event_type = payload.get("event")
        data = payload.get("data", {}).get("data", {})
        participant = data.get("participant", {})
        words_data = data.get("words", [])

        if not participant.get("id") or not words_data:
            return None

        participant_id = str(participant["id"])
        participant_name = participant.get("name", "Unknown")

        new_words = [
            Word(
                text=w.get("text", ""),
                start_timestamp=w.get("start_timestamp", {}).get("relative", 0.0),
                end_timestamp=w.get("end_timestamp", {}).get("relative") if w.get("end_timestamp") else None,
            )
            for w in words_data
        ]

        if event_type == "transcript.partial_data":
            return self._handle_partial_transcript(participant_id, participant_name, new_words)
        elif event_type == "transcript.data":
            return self._handle_final_transcript(participant_id, participant_name, new_words)
        
        return None

    def add_transcript_data(self, payload: dict) -> Tuple[str, TranscriptSegment]:
        """
        Process transcript.data event (finalized transcript).
        
        Returns:
            Tuple of (action_type, segment) where action_type is "MERGED" or "APPENDED"
        """
        data = payload.get("data", {}).get("data", {})
        participant = data.get("participant", {})
        words = data.get("words", [])

        if not participant.get("id") or not words:
            return None

        # Parse the new words
        new_words = []
        for word_data in words:
            word = Word(
                text=word_data.get("text", ""),
                start_timestamp=word_data.get("start_timestamp", {}).get(
                    "relative", 0.0
                ),
                end_timestamp=word_data.get("end_timestamp", {}).get("relative")
                if word_data.get("end_timestamp")
                else None,
            )
            new_words.append(word)

        participant_id = str(participant["id"])
        participant_name = participant.get("name", "Unknown")
        
        # Check if we should merge with the last segment
        if self.segments and new_words:
            last_segment = self.segments[-1]
            
            # Check merge criteria
            same_speaker = last_segment.participant_id == participant_id
            
            if same_speaker and last_segment.words and new_words[0].start_timestamp is not None:
                last_word_end = (last_segment.words[-1].end_timestamp or 
                               last_segment.words[-1].start_timestamp)
                time_gap = new_words[0].start_timestamp - last_word_end
                
                # If both criteria are met, merge
                if time_gap <= self.MERGE_THRESHOLD_SECONDS:
                    # Merge the words
                    last_segment.words.extend(new_words)
                    return ("MERGED", last_segment)
        
        # If we're not merging, create a new segment
        segment = TranscriptSegment(
            participant_id=participant_id,
            participant_name=participant_name,
            words=new_words,
            is_partial=False,
        )
        
        self.segments.append(segment)
        return ("APPENDED", segment)
    
    def _handle_partial_transcript(self, participant_id: str, participant_name: str, words: List[Word]) -> Tuple[str, TranscriptSegment, None]:
        """Handle partial transcript updates"""
        active_segment_id = self.active_partials.get(participant_id)

        if active_segment_id:
            # We have an active partial for this speaker, update it.
            try:
                # Find the segment to update. It should be the last one, but searching is safer.
                segment_to_update = next(s for s in reversed(self.segments) if s.id == active_segment_id)
                segment_to_update.words = words
                segment_to_update.timestamp = datetime.now()
                return "UPDATE", segment_to_update, None
            except StopIteration:
                # This case is unlikely but means our state is inconsistent.
                # We'll treat it as a new partial.
                pass

        # No active partial for this speaker, create a new one.
        new_segment = TranscriptSegment(
            participant_id=participant_id,
            participant_name=participant_name,
            words=words,
            is_partial=True,
        )
        self.segments.append(new_segment)
        self.active_partials[participant_id] = new_segment.id
        return "APPEND", new_segment, None
    
    def _handle_final_transcript(self, participant_id: str, participant_name: str, words: List[Word]) -> Tuple[str, TranscriptSegment, Optional[str]]:
        """Handle final transcript data"""
        active_segment_id = self.active_partials.get(participant_id)
        deleted_segment_id = None

        if active_segment_id:
            # This final transcript corresponds to a stream of partials we've been tracking.
            try:
                # Find the partial segment to finalize.
                segment_to_finalize = next(s for s in reversed(self.segments) if s.id == active_segment_id)
                segment_to_finalize.words = words
                segment_to_finalize.is_partial = False
                segment_to_finalize.timestamp = datetime.now()
                
                # Clean up the active partial tracking.
                del self.active_partials[participant_id]

                # Now, attempt to merge this newly finalized segment into the one before it.
                merged_segment, deleted_id = self._attempt_merge_with_previous(segment_to_finalize)
                if merged_segment:
                    return "MERGE_UPDATE", merged_segment, deleted_id
                
                # If no merge, just signal that the segment is now final.
                return "FINALIZE", segment_to_finalize, None

            except StopIteration:
                pass # Fall through to create a new final segment.
        
        # This is a standalone final transcript with no preceding partials.
        new_final_segment = TranscriptSegment(
            participant_id=participant_id,
            participant_name=participant_name,
            words=words,
            is_partial=False,
        )

        # Attempt to merge this new segment into the previous one.
        merged_segment, deleted_id = self._attempt_merge_with_previous(new_final_segment)
        if merged_segment:
            # The new segment was consumed by the merge, so we don't append it.
            # The deleted_id here will be the ID of the new_final_segment that was never truly added.
            return "MERGE_UPDATE", merged_segment, new_final_segment.id

        # No merge occurred, so append it as a new final segment.
        self.segments.append(new_final_segment)
        return "APPEND", new_final_segment, None
    
    def _attempt_merge_with_previous(self, current_segment: TranscriptSegment) -> Tuple[Optional[TranscriptSegment], Optional[str]]:
        """
        Checks if the current_segment can be merged with the last final segment in the store.
        If it can, it performs the merge and removes the current_segment from the list.
        
        Returns: (merged_segment, deleted_segment_id) if merge happened, else (None, None).
        """
        # Find the last non-partial segment to merge with.
        last_final_segment = None
        for segment in reversed(self.segments):
            if not segment.is_partial and segment != current_segment:
                last_final_segment = segment
                break
                
        if not last_final_segment or not last_final_segment.words:
            return None, None

        # Check merge criteria
        same_speaker = last_final_segment.participant_id == current_segment.participant_id
        if same_speaker and current_segment.words:
            last_word_end = (last_final_segment.words[-1].end_timestamp or
                             last_final_segment.words[-1].start_timestamp)
            
            time_gap = current_segment.words[0].start_timestamp - last_word_end
            
            if 0 <= time_gap <= self.MERGE_THRESHOLD_SECONDS:
                # Perform the merge
                last_final_segment.words.extend(current_segment.words)
                
                # If current_segment is already in the list, remove it.
                if current_segment in self.segments:
                    self.segments.remove(current_segment)
                
                return last_final_segment, current_segment.id

        return None, None


    def get_full_transcript(self) -> List[dict]:
        """Get the complete transcript"""
        transcript = []

        # Add all finalized segments
        for segment in self.segments:
            transcript.append(
                {
                    "id": segment.id,
                    "participant_id": segment.participant_id,
                    "participant_name": segment.participant_name,
                    "is_partial": segment.is_partial,
                    "words": [
                        {
                            "text": word.text,
                            "start_timestamp": word.start_timestamp,
                            "end_timestamp": word.end_timestamp,
                        }
                        for word in segment.words
                    ],
                    "timestamp": segment.timestamp.isoformat(),
                }
            )

        # Sort by first word timestamp
        transcript.sort(
            key=lambda s: s["words"][0]["start_timestamp"] if s["words"] else 0
        )

        return transcript

    def get_last_n_seconds(self, seconds: float) -> List[dict]:
        """Get transcript segments from the last N seconds"""
        if not self.segments:
            return []

        # Find the latest timestamp
        latest_timestamp = max(
            segment.words[-1].end_timestamp or segment.words[-1].start_timestamp
            for segment in self.segments
            if segment.words
        )

        cutoff_time = latest_timestamp - seconds

        # Filter segments
        recent_transcript = []
        for segment_data in self.get_full_transcript():
            words = segment_data["words"]
            if words and words[0]["start_timestamp"] >= cutoff_time:
                recent_transcript.append(segment_data)

        return recent_transcript

    def get_formatted_transcript(self) -> str:
        """Get a human-readable formatted transcript"""
        lines = []
        for segment_data in self.get_full_transcript():
            speaker = segment_data["participant_name"]
            partial_marker = " [partial]" if segment_data["is_partial"] else ""

            # Combine words into text
            text = " ".join(word["text"] for word in segment_data["words"])

            if segment_data["words"]:
                start_time = segment_data["words"][0]["start_timestamp"]
                end_time = segment_data["words"][-1]["end_timestamp"] or start_time
                lines.append(
                    f"{speaker}{partial_marker} ({start_time:.1f}s - {end_time:.1f}s): {text}"
                )

        return "\n".join(lines)
    
    def get_formatted_transcript_for_window(self, seconds: float) -> str:
        """Get a human-readable formatted transcript from the last N seconds."""
        recent_segments = self.get_last_n_seconds(seconds)
        if not recent_segments:
            return ""
        
        lines = []
        for segment_data in recent_segments:
            speaker = segment_data["participant_name"]
            text = " ".join(word["text"] for word in segment_data["words"])
            if text:  # Only add non-empty lines
                lines.append(f"{speaker}: {text}")
        
        return "\n".join(lines)
    
    def add_simulated_utterance(self, participant_name: str, text: str) -> TranscriptSegment:
        """
        Creates and adds a TranscriptSegment from a simulated text utterance.
        This provides a canonical way to represent simulated speech in the transcript.
        """
        # Determine the start time. If there's a previous segment, start after it.
        # Otherwise, start from 0.0. This creates a sequential timeline.
        last_end_time = 0.0
        if self.segments and self.segments[-1].words:
            last_word = self.segments[-1].words[-1]
            last_end_time = last_word.end_timestamp or last_word.start_timestamp
        
        # Approximate duration based on word count (e.g., 3 words per second)
        words_list = text.split()
        approx_duration = len(words_list) / 3.0
        
        start_time = last_end_time + 1.0 # Add a small buffer
        end_time = start_time + approx_duration

        # Create word objects with approximated timestamps
        segment_words = [
            Word(
                text=word,
                start_timestamp=start_time,
                end_timestamp=end_time
            ) for word in words_list
        ]

        segment = TranscriptSegment(
            # Use a consistent prefix for simulated participant IDs
            participant_id=f"simulated_{participant_name.lower().replace(' ', '_')}",
            participant_name=participant_name,
            words=segment_words,
            is_partial=False,
            timestamp=datetime.now()
        )
        self.segments.append(segment)
        return segment

    def clear(self):
        """Clear all transcript data"""
        self.segments.clear()
        self.active_partials.clear()


transcript_store = TranscriptStore()
