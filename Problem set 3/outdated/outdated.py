months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
         ]

# Take input in multiple formats
date = input("Date: ").strip()
while True:
    try:
        # Take an input , if key is not found in list then take input again
        month,day,year =date.split('/')
        if int(month) <= 12 and int(month) > 0 and int(day) > 0 and int(day) <= 31:
            break
    except:
        try:
            month,day,year = date.split()
            month = month.title()
            month = months.index(month) + 1
            if not day.endswith(","):
                continue
            day = day.replace("," , "")
            if int(month) <= 12 and int(month) > 0 and int(day) > 0 and int(day) <= 31:
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")