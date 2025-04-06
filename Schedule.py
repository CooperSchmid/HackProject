# Schedule.py
from sort import Sorter  # Import Sorter class from sort.py

class Schedule:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.time_slots = [
            "6am", "7am", "8am", "9am", "10am", "11am", "12pm",
            "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm"
        ]
        self.column_width = 20  # Consistent width for all columns
        self.entries = {
            time: {day: None for day in self.days}
            for time in self.time_slots
        }

    def add_sorter(self, sorter):
        """Add a Sorter object into the schedule at its specified day and time."""
        if sorter.day not in self.days:
            raise ValueError(f"Invalid day: {sorter.day}")

        # Map the time to the nearest hour
        hour_time = self.get_hour_from_time(sorter.time1)
        if hour_time not in self.entries:
            raise ValueError(f"Invalid time: {hour_time}")

        # Add sorter to the specified day
        self.entries[hour_time][sorter.day] = sorter

    def get_hour_from_time(self, time):
        """Converts a time (like 9:45am) to the nearest hour (e.g., 9am)."""
        time_mapping = {
            "6:00am": "6am", "6:15am": "6am", "6:30am": "6am", "6:45am": "6am",
            "7:00am": "7am", "7:15am": "7am", "7:30am": "7am", "7:45am": "7am",
            "8:00am": "8am", "8:15am": "8am", "8:30am": "8am", "8:45am": "8am",
            "9:00am": "9am", "9:15am": "9am", "9:30am": "9am", "9:45am": "9am",
            "10:00am": "10am", "10:15am": "10am", "10:30am": "10am", "10:45am": "10am",
            "11:00am": "11am", "11:15am": "11am", "11:30am": "11am", "11:45am": "11am",
            "12:00pm": "12pm", "12:15pm": "12pm", "12:30pm": "12pm", "12:45pm": "12pm",
            "1:00pm": "1pm", "1:15pm": "1pm", "1:30pm": "1pm", "1:45pm": "1pm",
            "2:00pm": "2pm", "2:15pm": "2pm", "2:30pm": "2pm", "2:45pm": "2pm",
            "3:00pm": "3pm", "3:15pm": "3pm", "3:30pm": "3pm", "3:45pm": "3pm",
            "4:00pm": "4pm", "4:15pm": "4pm", "4:30pm": "4pm", "4:45pm": "4pm",
            "5:00pm": "5pm", "5:15pm": "5pm", "5:30pm": "5pm", "5:45pm": "5pm",
            "6:00pm": "6pm", "6:15pm": "6pm", "6:30pm": "6pm", "6:45pm": "6pm",
            "7:00pm": "7pm", "7:15pm": "7pm", "7:30pm": "7pm", "7:45pm": "7pm",
            "8:00pm": "8pm", "8:15pm": "8pm", "8:30pm": "8pm", "8:45pm": "8pm"
        }
        return time_mapping.get(time, time)  # Defaults to time if not found

    def schedule_print(self):
        # Header with exact alignment
        header = f"{'Time':<6}|"
        for day in self.days:
            header += f"{day:^{self.column_width}}|"
        print(header)
        print("-" * len(header))

        for time in self.time_slots:
            # Gather and normalize lines for each column
            cell_lines = []
            max_lines = 0
            for day in self.days:
                sorter = self.entries[time][day]
                if sorter:
                    lines = str(sorter).split('\n')
                else:
                    lines = [""] * 4
                max_lines = max(max_lines, len(lines))
                cell_lines.append(lines)

            # Pad cells to same height
            for i in range(len(cell_lines)):
                while len(cell_lines[i]) < max_lines:
                    cell_lines[i].append("")

            # Print each line of the row
            for i in range(max_lines):
                row = f"{'':<6}|" if i != 0 else f"{time:<6}|"
                for col in cell_lines:
                    row += f"{col[i]:^{self.column_width}}|"
                print(row)

            # Separator line
            print("-" * len(header))
