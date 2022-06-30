def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if valid_length(s) and start_with_two_letters(s) and no_punction(s) and valid_numbers(s):
        return True
    return False

def start_with_two_letters(s):
    return s[0:2].isalpha()

def valid_length(s):
    return 2 <= len(s) <= 6

def no_punction(s):
    if s.isalnum():
        return True

def valid_numbers(s):
    # If the string has only letters no need to check for numbers, so continue
    if s.isalpha():
        return True

    # Check number of digits at the end
    number_of_digits = len([char for char in s if char.isdigit()]) # Count the number of digits in the string
    if s[-number_of_digits:].isnumeric(): # If the last digits are numbers continue else return False
        if s[-number_of_digits:][0] == "0": # If the first digit is 0 return False else return True
            return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
