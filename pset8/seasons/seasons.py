import re, sys, inflect

from datetime import date

p = inflect.engine()

def main():
    # Prompt the user for a date
    date_string = input("Enter a date (YYYY-MM-DD): ")
    # Validate the user input
    date_object = validate_date(date_string)
    # Get the number of minutes from the date to today
    minutes_since_midnight = (date.today() - date_object).total_seconds() / 60
    # Convert number of minutes to english words
    sentence = p.number_to_words(int(minutes_since_midnight))
    # Format the sentence removing "and", trailing spaces and capitalizing the first letter 
    sentence = sentence.replace(" and ", " ").strip().capitalize() 
    # Print the sentence and add "minutes" to the end
    print(sentence + " minutes")


def validate_date(string):
    # validate if the data is in the format YYYY-MM-DD using regex
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", string)

    # If valid date, return a date object
    if match:
        # Get year, month and day from regex expression
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        # Try to convert to date format, if invalid exit the code 
        try:
            return date(year, month, day)
        except ValueError:
            sys.exit("Invalid date! Verify year, month and day values.")
        return [year, month, day]
    else:
        sys.exit("Invalid date! Format should be in format YYYY-MM-DD")


if __name__ == "__main__":
    main()
