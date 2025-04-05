class Schedule(self): 
    print("----|----Monday----||----Tuesday----||----Wednesday----||----Thursday----||----Friday----|")
    for hour in range(4):
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print("-----              --               --                 --                --              |")
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print(f"{hour+6}am-|              ||               ||                 ||                ||              |")
    for hour in range(2):
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print("-----              --               --                 --                --              |")
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print(f"{hour+10}am|              ||               ||                 ||                ||              |")

    print("    |              ||               ||                 ||                ||              |")
    print("-----              --               --                 --                --              |")
    for i in range(2):
        print("    |              ||               ||                 ||                ||              |")
    print("12pm|              ||               ||                 ||                ||              |")
    for hour in range(9):
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print("-----              --               --                 --                --              |")
        for i in range(2):
            print("    |              ||               ||                 ||                ||              |")
        print(f"{hour+1}pm-|              ||               ||                 ||                ||              |")
