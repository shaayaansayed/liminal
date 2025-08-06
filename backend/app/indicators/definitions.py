# backend/app/indicators/definitions.py
from typing import TypedDict

class IndicatorDefinition(TypedDict):
    id: str
    name: str
    prompt_template: str
    # The rolling window of the transcript to analyze, in seconds
    window_seconds: int

# The prompt is carefully worded to elicit a structured "yes/no" response.
PACE_TOO_FAST_PROMPT = """You are a therapist observing a group session.
Your task is to determine if the conversation pace has been too fast in the last {window_seconds} seconds.
Consider factors like rapid speaking rate, quick topic shifts without resolution, or participants talking over each other.
Answer with only "yes" or "no", followed by a comma and a brief rationale.

Example: yes, the topic shifted from work to family matters very quickly.
Example: no, the conversation pace is appropriate.

Transcript:
<<<
{transcript_text}
>>>
"""

ALL_INDICATORS: list[IndicatorDefinition] = [
    {
        "id": "pace_too_fast",
        "name": "Pace Too Fast?",
        "prompt_template": PACE_TOO_FAST_PROMPT,
        "window_seconds": 120, # Analyze the last 2 minutes
    }
    # Future indicators can be added here
]