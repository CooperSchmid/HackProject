from sort import Sorter

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
        """Add a Sorter object into the schedule at its specified day and time1."""
        if sorter.day not in self.days:
            raise ValueError(f"Invalid day: {sorter.day}")
        if sorter.time1 not in self.entries:
            raise ValueError(f"Invalid time: {sorter.time1}")
        self.entries[sorter.time1][sorter.day] = sorter

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

# Example usage
s1 = Sorter("Math", "Room 101", "8am", "9am", "Mr. Smith", "Monday")
s2 = Sorter("Biology", "Lab A", "12pm", "1pm", "Dr. Reed", "Wednesday")
s3 = Sorter("History", "Room 202", "3pm", "4pm", "Mrs. Lane", "Friday")

sched = Schedule()
sched.add_sorter(s1)
sched.add_sorter(s2)
sched.add_sorter(s3)

sched.schedule_print()
