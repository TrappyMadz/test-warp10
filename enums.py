from enum import Enum

class SurvivorState(Enum):
    IDLE = "IDLE"
    CROUCHED = "CROUCHED"
    RUNNING = "RUNNING"
    REPAIRING = "REPAIRING"
    HEALING = "HEALING"
    CHASED = "CHASED"
    HOOKED = "HOOKED"
    CRAWLING = "CRAWLING"
    KILLER_INTERACTION = "KILLER INTERACTION"
    HIDING = "HIDING"
    DEAD = "DEAD"
    ESCAPED = "ESCAPED"

class KillerState(Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"
    CHASING = "IN CHASE"
    USING_POWER = "USING POWER"
    BREAKING = "BREAKING"
    STUNNED = "STUNNED"

class PalletState(Enum):
    READY = "READY"
    DROPPED = "DROPPED"
    BROKEN = "BROKEN"

class SurvivorHealthState(Enum):
    HEALTHY = "HEALTHY"
    INJURED = "INJURED"
    DEEP_WOUND = "DEEP_WOUND"
    DYING = "DYING"