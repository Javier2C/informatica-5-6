from datetime import datetime

def main():


    day = datetime.now().weekday()
    days = ["monday", "tuesday", "wednesday", "thrusday", "friday","saturday", "sunday"]
    print(days[day])

    if day < 4:
        print("its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("its just friday")
        print("just a day left until the weekend")
    else:
        print("its a weekend")
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    #print("these are the summer months:")
    #print(months[5])
    #print(months[6])
    #print(months[7])
    month = datetime.now().month
    print("it is", months[month-1])




if __name__ == "__main__":
    main()
