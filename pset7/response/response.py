import validators


def main():
    print(validate_email(input("Email: ")))


def validate_email(s):
    # Validate email adress s with validators library
    return "Valid" if validators.email(s) else "Invalid"


if __name__ == "__main__":
    main()