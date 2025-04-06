# sort.py
class Sorter:
    def __init__(self, title, location, time1, time2, teacher, day):
        self.title = title 
        self.location = location 
        self.time1 = time1 
        self.time2 = time2 
        self.teacher = teacher
        self.day = day 

    def __str__(self):
        width = 20
        
        time_str = ""
        if self.time1 and self.time2:
            time_str = f"{self.time1}-{self.time2}"
        elif self.time1:
            time_str = self.time1
        elif self.time2:
            time_str = self.time2

        line = []

        if self.title:
            line.append(self.title.upper().center(width))
        if self.location:
            line.append(self.location.upper().center(width))
        if time_str:
            line.append(time_str.center(width))
        if self.teacher:
            line.append(self.teacher.center(width))
        if self.day:
            line.append(self.day.center(width))

        x = '\n'.join(line)
        return x

 
    


        
    
    
    
