def main():
    # Ask the user for a meal time
    meal_time = input("What time is it? ").lower()
    # Convert the meal time to a number
    meal_time = convert(meal_time)
    # Check wheter it's breakfast time, lunch time, or dinner time
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")



def convert(time):
    # Convert the time to a number (0-23)
    # Try to convert the time to a number if a.m. or p.m. is present
    try:
        time, am_pm = time.split(" ")
        hours, minutes = time.split(":")
        if am_pm == "p.m.":
            hours = int(hours) + 12
        else:
            hours = int(hours)
    # If a.m. or p.m. is not present, just convert the time to a number
    except:
        hours, minutes = time.split(":")

    # Convert the minutes to a number
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()