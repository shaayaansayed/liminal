# backend/zoom_turnflow.py
from enum import Enum, auto
from dataclasses import dataclass
from datetime import datetime, timezone
import asyncio
import logging

logger = logging.getLogger(__name__)


class TurnPhase(Enum):
    READY = auto()          # room quiet ≥ SILENCE_S
    PLAYING = auto()        # TTS-MP3 was just pushed to Recall
    TRANSCRIBING = auto()   # first transcript packet arrived


@dataclass
class MeetingState:
    phase: TurnPhase = TurnPhase.READY
    last_ts: datetime | None = None        # latest transcript timestamp


MEETING = MeetingState()                   # singleton – import-once pattern
SILENCE_S = 3.0


async def turnflow_monitor() -> None:
    """Transitions PLAYING → TRANSCRIBING → READY by timing silence gaps."""
    while True:
        await asyncio.sleep(0.25)
        if MEETING.phase is TurnPhase.TRANSCRIBING:
            gap = (datetime.now(timezone.utc) - MEETING.last_ts).total_seconds()
            if gap > SILENCE_S:
                logger.info("Silence ≥ %.1fs → READY", SILENCE_S)
                MEETING.phase = TurnPhase.READY