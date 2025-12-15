from room import Room
from file_manager import save_room, load_rooms
from validators import is_positive_number

def manage_rooms():
    rooms = load_rooms()

    print("1. Add Room")
    print("2. View Rooms")
    choice = input("Choice: ")

    if choice == "1":
        room_num = input("Room number: ")
        name = input("Room name: ")
        capacity = input("Capacity: ")
        building = input("Building: ")

        if not is_positive_number(capacity):
            print("Invalid capacity")
            return

        room = Room(room_num, name, int(capacity), building)
        save_room(room)
        print("Room added.")

    elif choice == "2":
        for r in rooms:
            print(r.get_room_num(), r.get_name(), r.get_status())
