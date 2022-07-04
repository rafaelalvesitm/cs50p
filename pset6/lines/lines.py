import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py <filename.py>")

    try:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.exit("File not found: " + sys.argv[1])

    number_of_lines = 0
    for line in lines:
        if line.lstrip().startswith("#") or line.strip() == "":
            continue
        number_of_lines += 1
    print(number_of_lines)

if __name__ == '__main__':
    main()