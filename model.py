from pydantic import BaseModel, Field
from typing import Dict
from enum import Enum
import time

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


class SurvivorPosition(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.playerX.position"
    labels: Dict[str, str] # {username: "gamerX", character: "Jill Valentine, map: "Nostromo Wreckage", held_item: "none", health: "injured"}
    lat: float # player.position.x
    lon: float # player.position.y
    value: SurvivorState # IDLE 

class KillerPosition(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.killer.position"
    labels: Dict[str, str] # {username: "gamerX", character: "The Trapper, map: "Nostromo Wreckage"}
    lat: float # player.position.x
    lon: float # player.position.y
    value: KillerState # IDLE 

class GeneratorAdvancement(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.generator.state"
    labels: Dict[str, str] # {generatorId = "0"}
    lat: float # generators[0].position.x
    lon: float # generators[0].position.y
    value: int # 55 (%) 

class ExitDoorsAdvancement(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.exitdoor.state"
    labels: Dict[str, str] # {exitdoorId = "0"}
    lat: float # exitdoors[0].position.x
    lon: float # exitdoors[0].position.y
    value: int # 55 (%) 

class PerkActivation(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.perk.activation"
    labels: Dict[str, str] # {perkName: "sprint_burst", bonus: "50% haste", duration: "3", malus: "Exhausted for 40s"}
    lat: float # player.position.x
    lon: float # player.position.y
    value: str # "ACTIVATED"

class PalletUsage(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.pallet.usage"
    labels: Dict[str, str] # {palletId: 11}
    lat: float # pallet.position.x
    lon: float # pallet.position.y
    value: PalletState

class HookState(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.hook.usage"
    labels: Dict[str, str] # {hookId: 4, victim: "Steve Harrington"}
    lat: float # hook.position.x
    lon: float # hook.position.y
    value: int # 2 (number of times victim has been hooked)