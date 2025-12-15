from file_manager import load_rooms, load_events

def generate_reports():
    print("\nROOM REPORT")
    for r in load_rooms():
        print(r.get_room_num(), r.get_status())

    print("\nEVENT REPORT")
    for e in load_events():
        print(e.get_name(), e.get_date(), e.get_time(), e.get_room_num())
