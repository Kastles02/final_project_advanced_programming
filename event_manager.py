import event
def main_event():
    events = []
    user = input("Welcome to the Event Manager! Choose from the following menu options.\n1.Check Events\n2.Add Event\n3.Modify Event\n4.Delete Event")
    if user == 1:
        for item in event:
                print(f"Name: {event.get_name()}")
                print(f"Room Number: {event.get_room_num()}")
                print(f"Club Name: {event.get_club_name()}")
                print(f"Event Time: {event.get_event_time()}")
                print(f"Average/Estimated Attendance: {event.get_avg_atten()}")
                print(f"Contact Information: {event.get_contact_info()}")
                print()
    elif user = 2:
        name = input("Enter the Event Name.")
        room_num = input("Enter the Room Number the event will be in.")
        club_name = input("Enter the Club Name.")
        event_time = input("Enter the Event Time")
        avg_atten = input("Enter the amount of students you expect to attend the Event.")
        contact_info = input("Enter the Contact Information for the president or supervisor of the event.")
        events.append(Event(name,room_num,club_name,event_time,avg_atten,contact_info))
    elif user = 3:
        count = 0
        for item in events:


