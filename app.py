import requests
from dotenv import load_dotenv
import os
from models import *
import time

load_dotenv()
WRITE_TOKEN = os.getenv("WARP10_WT")
READ_TOKEN = os.getenv("WARP10_RT")
URL = "http://localhost:8080/api/v0/"

def label_formatter(label_obj):
    """
    Take a label pydantic object and convert it to str for Warp10. 
    Also convert the uuid in str
    """

    label_dict = label_obj.model_dump(exclude_none=True)

    tuple_list = []

    for key, value in label_dict.items():
        if hasattr(value, 'value'):
            formatted_value = value.value
        else:
            formatted_value = value

        tuple_list.append(f"{key}={str(formatted_value)}")

    return ",".join(tuple_list)

def value_formatter(value):
    """
    Format the value for Wrap10. Add "" if needed (a string)
    """

    # is the data is an enum ?
    if hasattr(value, 'value'):
        return f'"{value.value}"'
    else:
        return value


def create_point(data_obj):
    """
    Take a pydantic object and send it to /update
    """
    formatted_labels = label_formatter(data_obj.labels)
    formatted_value = value_formatter(data_obj.value)

    gts_line = (
        f"{data_obj.timestamp}/{data_obj.lat}:{data_obj.lon}/ "
        f"{data_obj.name}{{{formatted_labels}}} {formatted_value}"
    )

    headers = {"X-Warp10-Token": WRITE_TOKEN}
    response = requests.post(URL + "update", data=gts_line, headers=headers)

    if response.status_code == 200:
        print(f"Point saved : {data_obj.name}")
        return True
    else:
        print(f"ERROR : {response.status_code} : {response.text}")
        return False

def read_points(selector, number_of_points=10):
    """
    Take a series name and a number of points to return.
    series name exemple : dbd.generator.state{id=15}
    you can select all the series of one category :
    dbd.hook.state{}

    this function return the most recent "number_of_points" points.
    """

    parameters = {
        "token": READ_TOKEN,
        "selector": selector,
        "now": "now",
        "timespan": -number_of_points
    }
    response = requests.get(URL + "fetch", params=parameters)

    if response.status_code == 200:
        print(f"--- RETRIEVED DATA FOR {selector} ---")
        print(response.text)
        return response.text
    else:
        print(f"ERROR : {response.status_code} : {response.text}")
        return None

def update_point(data_obj):
    """
    For time series, there is no update, so make sure the timestamp and name
     of the new objects are the exact same as the one you want to update.
     Note that time series are not made with update in mind, so it could
     break data consistency.
    """
    return create_point(data_obj)

def delete_points(selector):
    """
    Delete all data concerning a specific data.
    """
    
    end = int(time.time() * 1000000)

    parameters = {
        "token": WRITE_TOKEN,
        "selector": selector,
        "start": 0,
        "end": end
    }

    response = requests.get(URL + "delete", params=parameters)
        
    if response.status_code == 200:
        print(f"Successfully deleted {selector}.")
        return True
    else:
        print(f"ERROR : {response.status_code} : {response.text}")
        return False