import room
def main_room():
    rooms = []
    user = input("Welcome to the Room Manager! Choose from the following menu options.\n1.Check Rooms\n2.Add Room\n3.Modify Room\n4.Delete Room")
    if user == 1:
        for item in event:
                print(f"Name: {room.get_name()}")
                print(f"Room Number: {room.get_room_num()}")
                print(f"Room Size: {room.get_size()}")
                print(f"Amount of Computers: {room.get_computers()}")
                print(f"Amount of people able to fit in the room: {room.get_person_size()}")
                print(f"Is the room Available?: {room.get_availability()}")
                print(f"Projector?: {room.get_projector()}")
                print()
    elif user = 2:
        name = input("Enter the building name.")
        room_num = input("Enter the Room Number.")
        size = input("Enter the Room Size.")
        computers = input("Enter the number of Computers.")
        person_size = input("Enter the amount of students able to fit in the room.")
        availability = input("Enter if the room is available.")
        projector = input("Enter if the room has a projector.")
        events.append(Room(name,size,computers,person_size,availability,projector,room_num))
    elif user = 3:
        count = 0
        for item in rooms: