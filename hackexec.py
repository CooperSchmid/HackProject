# Executive.py
from Schedule import Schedule  # Import Schedule class from Schedule.py
from sort import Sorter  # Import Sorter class from sort.py

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
            time1 = input("Start Time (e.g., 9:00am, 9:15am, etc.): ")
            time2 = input("End Time (e.g., 10:00am, 10:15am, leave blank for single time): ")
            teacher = input("Teacher's Name: ")
            days_input = input("Days (e.g., Monday, Wednesday, Friday): ")
            days = [day.strip() for day in days_input.split(',') if day.strip() in self.schedule.days]

            # Add the course for each day
            for day in days:
                sorter = Sorter(title, location, time1, time2, teacher, day)
                try:
                    self.schedule.add_sorter(sorter)
                    print(f"Course '{title}' added to schedule for {day}.")
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

# Execute the program
if __name__ == "__main__":
    executive = Executive()
    executive.run()


