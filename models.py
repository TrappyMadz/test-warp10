from pydantic import BaseModel, Field
from typing import Dict, List, Optional
import time
from enums import *
from label import Label


class SurvivorPosition(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.player.position"
    labels: Label
    lat: float # player.position.x
    lon: float # player.position.y
    value: SurvivorState # IDLE 

class KillerPosition(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.killer.position"
    labels: Label
    lat: float # player.position.x
    lon: float # player.position.y
    value: KillerState # IDLE 

class GeneratorAdvancement(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.generator.state"
    labels: Label
    lat: float # generators[0].position.x
    lon: float # generators[0].position.y
    value: int # 55 (%) 

class ExitDoorsAdvancement(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.exitdoor.state"
    labels: Label
    lat: float # exitdoors[0].position.x
    lon: float # exitdoors[0].position.y
    value: int # 55 (%) 

class PerkActivation(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.perk.activation"
    labels: Label
    lat: float # player.position.x
    lon: float # player.position.y
    value: str # "ACTIVATED"

class PalletUsage(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.pallet.usage"
    labels: Label
    lat: float # pallet.position.x
    lon: float # pallet.position.y
    value: PalletState

class HookState(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str # "dbd.hook.usage"
    labels: Label
    lat: float # hook.position.x
    lon: float # hook.position.y
    value: int # 2 (number of times victim has been hooked)

class SurvivorHealth(BaseModel):
    timestamp: int = Field(default_factory=lambda: int(time.time() * 1000000))
    name: str
    labels: Label
    lat: float 
    lon: float 
    value: SurvivorHealthState