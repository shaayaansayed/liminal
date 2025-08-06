from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Word:
    text: str
    start_timestamp: float
    end_timestamp: Optional[float] = None


@dataclass
class TranscriptSegment:
    participant_id: str
    participant_name: str
    words: List[Word] = field(default_factory=list)
    is_partial: bool = False
    timestamp: datetime = field(default_factory=datetime.now)


class TranscriptStore:
    def __init__(self):
        self.segments: List[TranscriptSegment] = []
        self.partial_segments: Dict[str, TranscriptSegment] = {}

    def add_transcript_data(self, payload: dict):
        """Process transcript.data event (finalized transcript)"""
        data = payload.get("data", {}).get("data", {})
        participant = data.get("participant", {})
        words = data.get("words", [])

        if not participant.get("id") or not words:
            return

        # Convert partial segment to final if exists
        participant_id = str(participant["id"])
        if participant_id in self.partial_segments:
            segment = self.partial_segments.pop(participant_id)
            segment.is_partial = False
        else:
            segment = TranscriptSegment(
                participant_id=participant_id,
                participant_name=participant.get("name", "Unknown"),
                is_partial=False,
            )

        # Add words to segment
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
            segment.words.append(word)

        self.segments.append(segment)

    def add_partial_transcript_data(self, payload: dict):
        """Process transcript.partial_data event (interim transcript)"""
        data = payload.get("data", {}).get("data", {})
        participant = data.get("participant", {})
        words = data.get("words", [])

        if not participant.get("id") or not words:
            return

        participant_id = str(participant["id"])

        # Create or update partial segment
        segment = TranscriptSegment(
            participant_id=participant_id,
            participant_name=participant.get("name", "Unknown"),
            is_partial=True,
        )

        # Add words
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
            segment.words.append(word)

        self.partial_segments[participant_id] = segment

    def get_full_transcript(self) -> List[dict]:
        """Get the complete transcript including partial segments"""
        transcript = []

        # Add all finalized segments
        for segment in self.segments:
            transcript.append(
                {
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

        # Add current partial segments
        for segment in self.partial_segments.values():
            transcript.append(
                {
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
        self.partial_segments.clear()


transcript_store = TranscriptStore()
