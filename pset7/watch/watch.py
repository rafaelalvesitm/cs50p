import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Check if there is an iframe in the string
    if re.search(r"iframe", s):
        # Try to get the url from the iframe
        try:
            url = re.search(r"https?://(www\.)?youtube\.com/embed/\w+", s).group(0)
        except AttributeError:
            return None
        
        # If the url is found get the last part of the url and return shorten url
        if url:
            link = url.split("/")[-1]
            return f"https://youtu.be/{link}"
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()
