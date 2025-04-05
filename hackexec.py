from schedule import Schedule
from sort import Sorter

class Executive:
    def __init__(self):
        self.schedule = Schedule()

    def get_user_input(self):
        """Collects user input for scheduling courses."""
        while True:
            print("Enter course details:")
            title = input("Course Title (or type 'done' to finish): ")
            if title.lower() == 'done':
                break
            location = input("Location: ")
            time1 = input("Start Time (e.g., 9am): ")
            time2 = input("End Time (e.g., 10am, leave blank for single time): ")
            teacher = input("Teacher's Name: ")
            day = input("Day (e.g., Monday): ")

            sorter = Sorter(title, location, time1, time2, teacher, day)
            try:
                self.schedule.add_sorter(sorter)
                print(f"Course '{title}' added to schedule.")
            except ValueError as e:
                print(f"Error: {e}")

    def display_schedule(self):
        """Displays the full schedule."""
        self.schedule.schedule_print()

    def run(self):
        """Runs the executive process for schedule creation."""
        print("Welcome to the Schedule Creator!")
        self.get_user_input()
        print("\nHere is your final schedule:\n")
        self.display_schedule()


main()
executive = Executive()
executive.run()
