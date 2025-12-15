from file_manager import load_events, load_rooms, save_event
from event import Event

def event_conflict(room_num, date, time):
    events = load_events()
    for e in events:
        if e.get_room_num() == room_num and e.get_date() == date and e.get_time() == time:
            return True
    return False

def add_event(event):
    if event_conflict(event.get_room_num(), event.get_date(), event.get_time()):
        print("Scheduling conflict detected!")
        return
    save_event(event)
    print("Event scheduled.")



