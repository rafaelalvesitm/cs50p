import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Count the number of times "um" appears in the string s.
    # Um should only be counted if it appears as a word and not in the middle of a word link in cirumscription
    return len(re.findall(r"\bum\b", s.lower()))


if __name__ == "__main__":
    main()