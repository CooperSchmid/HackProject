from sort import Sorter

class Schedule:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.time_slots = [
            "6am", "7am", "8am", "9am", "10am", "11am", "12pm",
            "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm"
        ]
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
        # Header
        print("----|----Monday----||----Tuesday----||----Wednesday----||----Thursday----||----Friday----|")

        for time in self.time_slots:
            # Gather the display lines for each column (day)
            cell_lines = []
            max_lines = 0
            for day in self.days:
                sorter = self.entries[time][day]
                if sorter:
                    lines = str(sorter).split('\n')
                else:
                    lines = [""] * 4  # Reserve space for empty slots
                max_lines = max(max_lines, len(lines))
                cell_lines.append(lines)

            # Normalize all cells to have same number of lines
            for i in range(len(cell_lines)):
                if len(cell_lines[i]) < max_lines:
                    cell_lines[i] += [""] * (max_lines - len(cell_lines[i]))

            # Print each line of the block
            for i in range(max_lines):
                row = "    |"
                for day_idx in range(len(self.days)):
                    content = cell_lines[day_idx][i]
                    row += f"{content[:14]:^14}||"
                print(row[:-1])  # Remove trailing pipe

            # Separator line
            print(f"{time:<4}-{'-' * 96}")
