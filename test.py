import uuid
from models import SurvivorPosition
from enums import SurvivorState, SurvivorHealthState
from label import Label
import time
from app import create_point, read_points

# Match id generation
match_id = uuid.uuid4()
survivor_id = uuid.uuid4()

# test with a survivor position
# creating survivor position
label = Label(
    entity_id = survivor_id,
    match_id = match_id,
    map = "freddy_fazbear_s_pizza",
    username = "Madz",
    character = "jill_valentine",
    held_item = "first_care_kit",
    health_state = SurvivorHealthState.INJURED
)
survivor_position = SurvivorPosition(
    name = "dbd.survivor.position",
    labels = label,
    lat = 4.0,
    lon = 11.5,
    value = SurvivorState.CHASED
)

# create point
create_point(survivor_position)

# sleep a litle
time.sleep(10)

# read point
read_points(f"dbd.survivor.position{{entity_id={survivor_id}}}")