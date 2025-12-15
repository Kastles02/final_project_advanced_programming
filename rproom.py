# roomsreport.py
# This script loads Room objects from room.txt
# and writes a simple report to roomsreport.txt

from room import Room   # import Room class

ROOMS_FILE = "room.txt"           # file where rooms are stored
OUTPUT_FILE = "roomsreport.txt"   # file to save report


def load_rooms():
    rooms = []  # list to hold Room objects

    try:
        file = open(ROOMS_FILE, "r")  # open rooms file
        for line in file:
            # Each line: name|size|computers|person_size|availability|projector|room_num
            parts = line.strip().split("|")
            if len(parts) == 7:  # make sure all fields exist
                name = parts[0]
                size = parts[1]
                computers = parts[2]
                person_size = parts[3]
                availability = parts[4]
                projector = parts[5]
                room_num = parts[6]

                # create Room object
                room = Room(name, size, computers, person_size, availability, projector, room_num)
                rooms.append(room)  # add to list

        file.close()  # close file after reading

    except:  # if file missing or cannot open
        pass

    return rooms  # return the list of Room objects


def generate_rooms_report():
    rooms = load_rooms()  # get all Room objects

    rp = open(OUTPUT_FILE, "w")  # open report file
    rp.write("ROOM REPORT\n")
    

    for r in rooms:  # loop through rooms and write details
        rp.write(f"Room Number: {r.get_room_num()}\n")
        rp.write(f"Name: {r.get_name()}\n")
        rp.write(f"Size: {r.get_size()}\n")
        rp.write(f"Computers: {r.get_computers()}\n")
        rp.write(f"Person Capacity: {r.get_person_size()}\n")
        rp.write(f"Availability: {r.get_availability()}\n")
        rp.write(f"Projector: {r.get_projector()}\n")
       

    rp.close()  # close the report file
    return OUTPUT_FILE
# Run the report directly if this script is executed
if __name__ == "__main__":
    filename = generate_rooms_report()
    print(f"Room report generated: {filename}")
