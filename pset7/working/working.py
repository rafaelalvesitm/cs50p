import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Get work hours in the possible formats
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM

    # Check if the string is in the correct format
    match = re.search(r"(\d{1,2}:\d{1,2}|\d{1,2}) ([AP]M) to (\d{1,2}:\d{1,2}|\d{1,2}) ([AP]M)", s)
    if match:
        # Get the start and end time
        start = match.group(1)
        start_am_pm = match.group(2)
        end = match.group(3)
        end_am_pm = match.group(4)
        
        # if : in the start time, get hours and minutes else minutes are 0
        if ":" in start:
            start_hours = int(start.split(":")[0])
            start_minutes = int(start.split(":")[1])
        else:
            start_hours = int(start)
            start_minutes = 0
        
        if ":" in end:
            end_hours = int(end.split(":")[0])
            end_minutes = int(end.split(":")[1])
        else:
            end_hours = int(end)
            end_minutes = 0

        # Check if hours and minutes are in the correct range
        if start_hours < 0 or start_hours > 13 or start_minutes < 0 or start_minutes > 59:
            raise ValueError("Start time is not in the correct format")
        if end_hours < 0 or end_hours > 13 or end_minutes < 0 or end_minutes > 59:
            raise ValueError("End time is not in the correct format")
        
        # Convert to 24 hour format
        if start_am_pm == "PM" and start_hours != 12:
            start_hours += 12
        if end_am_pm == "PM" and end_hours != 12:
            end_hours += 12
        if start_am_pm == "AM" and start_hours == 12:
            start_hours -= 12
        if end_am_pm == "AM" and end_hours == 12:
            end_hours -= 12

        # Return formated string as "HH:MM to HH:MM"
        return(f"{start_hours:02}:{start_minutes:02} to {end_hours:02}:{end_minutes:02}")
    else:
        raise ValueError("String is not in the correct format")

   


if __name__ == "__main__":
    main()