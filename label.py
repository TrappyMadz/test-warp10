from pydantic import BaseModel, Field
from typing import Optional
import uuid
from enums import SurvivorHealthState

class Label(BaseModel):
    entity_id: uuid.UUID
    match_id: uuid.UUID
    map: str

    username: Optional[str] = None
    character: Optional[str] = None
    perk_name: Optional[str] = None
    perk_effect: Optional[str] = None
    perk_duration: Optional[int] = None
    hook_victim: Optional[str] = None
