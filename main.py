from menu import menu

def main():
    while True:
        choice = menu()
        if choice == "1":
            from manage_rooms import manage_rooms
            manage_rooms()
        elif choice == "2":
            from add_event import prompt_add_event
            prompt_add_event()
        elif choice == "3":
            from reports import generate_reports
            generate_reports()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
