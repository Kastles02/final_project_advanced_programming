from room import Room
from event import Event

ROOM_FILE = "rooms.txt"
EVENT_FILE = "events.txt"

def save_room(room):
    with open(ROOM_FILE, "a") as f:
        f.write(f"{room.get_room_num()}|{room.get_name()}|{room.get_capacity()}|{room.get_building()}|{room.get_status()}\n")

def load_rooms():
    rooms = []
    try:
        with open(ROOM_FILE, "r") as f:
            for line in f:
                r = line.strip().split("|")
                rooms.append(Room(r[0], r[1], int(r[2]), r[3], r[4]))
    except:
        pass
    return rooms

def save_event(event):
    with open(EVENT_FILE, "a") as f:
        f.write(f"{event.get_name()}|{event.get_club()}|{event.get_room_num()}|{event.get_date()}|{event.get_time()}|{event.get_attendance()}\n")

def load_events():
    events = []
    try:
        with open(EVENT_FILE, "r") as f:
            for line in f:
                e = line.strip().split("|")
                events.append(Event(e[0], e[1], e[2], e[3], e[4], int(e[5])))
    except:
        pass
    return events
