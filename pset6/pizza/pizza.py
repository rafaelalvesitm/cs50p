import sys, tabulate, csv

def main():
    # Read command line arguments expecting "python3 pizza.py <filename.csv>""
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Usage: python pizza.py <filename.csv>")

    # Read the csv file and store it in a list
    menu = list()
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File not found: " + sys.argv[1])

    # Print a table formated with tabulate and grid mode
    print(tabulate.tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == '__main__':
    main()