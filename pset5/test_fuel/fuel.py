def main():
    # Reapeat until the user provides an valid input in the form x/y
    while True:
        input_string = input("Fraction: ")
        try:
            percentage = convert(input_string)
            print(gauge(percentage))
            break
        except:
            continue


def convert(fraction):
    # Convert the fraction to a percentage as an integer
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except:
        raise ValueError("Invalid fraction")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    elif x > y:
        raise ValueError("Invalid fraction")

    return round(x / y * 100)


def gauge(percentage):
    # Show gauge
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
