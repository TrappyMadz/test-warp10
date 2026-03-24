import time
import uuid
from enums import *
from label import Label
from models import *
from app import create_point 

print("Starting simulation...")

match_uuid = uuid.uuid4()
map_name = "macmillan_estate"
killer_id = uuid.uuid4()

survivors = {
    "dwight": {"id": uuid.uuid4(), "username": "PizzaLover", "char": "dwight_fairfield"},
    "meg": {"id": uuid.uuid4(), "username": "TrackStar", "char": "meg_thomas"},
    "claudette": {"id": uuid.uuid4(), "username": "Healz0rz", "char": "claudette_morel"},
    "nea": {"id": uuid.uuid4(), "username": "UrbanEvader", "char": "nea_karlsson"}
}

gen_id = uuid.uuid4()
door_id = uuid.uuid4()

def send_survivor_action(name, state, lat, lon):
    """Send action and position"""
    s = survivors[name]
    lbl = Label(entity_id=s["id"], match_id=match_uuid, map=map_name, username=s["username"], character=s["char"])
    pt = SurvivorPosition(name="dbd.survivor.position", labels=lbl, lat=lat, lon=lon, value=state)
    create_point(pt)

def send_survivor_health(name, health_state, lat, lon):
    """Send health state"""
    s = survivors[name]
    lbl = Label(entity_id=s["id"], match_id=match_uuid, map=map_name, username=s["username"], character=s["char"])
    pt = SurvivorHealth(name="dbd.survivor.health", labels=lbl, lat=lat, lon=lon, value=health_state)
    create_point(pt)

def send_killer_update(state, lat, lon):
    lbl = Label(entity_id=killer_id, match_id=match_uuid, map=map_name, character="the_trapper")
    pt = KillerPosition(name="dbd.killer.position", labels=lbl, lat=lat, lon=lon, value=state)
    create_point(pt)

def send_generator_update(progress):
    lbl = Label(entity_id=gen_id, match_id=match_uuid, map=map_name)
    pt = GeneratorAdvancement(name="dbd.generator.state", labels=lbl, lat=11.0, lon=15.5, value=progress)
    create_point(pt)

for name in survivors.keys():
    send_survivor_health(name, SurvivorHealthState.HEALTHY, 0.0, 0.0)

print("\nRepairing...")
for i in range(1, 4):
    send_survivor_action("dwight", SurvivorState.REPAIRING, 11.0, 15.0)
    send_survivor_action("meg", SurvivorState.REPAIRING, 11.0, 16.0)
    send_survivor_action("claudette", SurvivorState.RUNNING, 40.0 - i, 40.0)
    send_survivor_action("nea", SurvivorState.CROUCHED, 45.0, 42.0)
    
    send_killer_update(KillerState.MOVING, 30.0 + i, 30.0 + i)
    send_generator_update(i * 33)
    time.sleep(1)

print("\nThe trapper get to Claudette !")
send_killer_update(KillerState.CHASING, 38.0, 39.0)
send_survivor_action("claudette", SurvivorState.CHASED, 38.0, 40.0)
time.sleep(1)

print("Claudette was hit !")
send_killer_update(KillerState.USING_POWER, 38.5, 40.0)
send_survivor_action("claudette", SurvivorState.RUNNING, 39.0, 42.0)
send_survivor_health("claudette", SurvivorHealthState.INJURED, 39.0, 42.0)
time.sleep(1)

print("\nGenerator, opening exit gates")
send_generator_update(100)
time.sleep(1)

lbl_door = Label(entity_id=door_id, match_id=match_uuid, map=map_name)
create_point(ExitDoorsAdvancement(name="dbd.exitdoor.state", labels=lbl_door, lat=5.0, lon=5.0, value=100))

print("Alive survivors are escaping...")
send_survivor_action("dwight", SurvivorState.ESCAPED, 5.0, 5.0)
send_survivor_action("meg", SurvivorState.ESCAPED, 5.0, 5.0)
send_survivor_action("nea", SurvivorState.ESCAPED, 5.0, 5.0)
send_survivor_action("claudette", SurvivorState.HIDING, 39.0, 42.0) # Elle se cache, toujours blessée

print("\nEnding simulation")
print(f"match id : {match_uuid}")