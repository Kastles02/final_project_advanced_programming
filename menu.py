from manage_rooms import manage_rooms
from add_event import prompt_add_event
from reports import generate_reports

def menu():
    print("\n--- Amarillo College Scheduler ---")
    print("1. Manage Rooms")
    print("2. Add Event")
    print("3. Reports")
    print("4. Exit")

    return input("Select: ")
