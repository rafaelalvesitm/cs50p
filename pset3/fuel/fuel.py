def main():
    # Reapeat until the user provides an valid input in the form x/y
    while True:
        # Try to get user's input, if it fails, reprompt the user
        try:
            numerator, denominator = input("Fraction: ").split("/")
        except:
            continue
        # Try to convert the input to integers, if it fails, reprompt the user
        try: 
            int(numerator)
        except:
            continue
        # Try to convert the input to integers, if it fails, reprompt the user
        try:
            int(denominator)
        except:
            continue
        # Try to create a fraction from the input, if it fails, reprompt the user
        try:
            fraction = int(numerator)/int(denominator)
        except (ValueError, ZeroDivisionError):
            continue

        # If the fraction is a valid fraction, break the loop, otherwise reprompt the user
        if fraction > 1:
                continue
        elif fraction >= 0.99:
            print("F")
        elif fraction <= 0.01:
            print("E")
        else:
            print(f"{round(fraction *100)}%")
        break
    

if __name__ == "__main__":
    main()