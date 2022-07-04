import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Validate IPV4 address
    # Remember regex simbols
    # ^ = start of string
    # $ = end of string
    # \d = digit
    # {1,3} = 1 to 3 of something
    # \. = period
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        # Split IP into small parts
        parts = ip.split(".")
        # Validate each octet
        for part in parts:
            if int(part) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()