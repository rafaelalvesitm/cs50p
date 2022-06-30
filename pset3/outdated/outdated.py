import sys

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

def main():
    # prompts the user for a date
    while True:
        # Ask for the user to input a date
        date = input("Date: ")

        # Check if the input is in the format month/day/year or monnth day, year.

        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")

            if month in months: 
                month = months.index(month) + 1
        else:
            continue

        try:
            if int(month) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue


    print(f"{int(year):04}-{int(month):02}-{int(day):02}")


if __name__ == "__main__":
    main()
