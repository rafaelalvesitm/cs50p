import sys, csv

def main():
    # Read command line arguments expecting "python3 pizza.py <filename.csv>""
    if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Usage: python scourgify.py <filename.csv> <filename.csv>")

    # Read the csv file and store it in a list
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({'name': row['name'], 'house': row['house']})
    except FileNotFoundError:
        sys.exit("File not found: " + sys.argv[1])
    
    # Separeta first and last name for each person in the data
    for row in data:
        last, first = row['name'].split(",")
        row['first'] = first.strip()
        row['last'] = last.strip()
        row.pop('name')
    
    # Write the data (first, last, house) to a new csv file 
    try:
        with open(sys.argv[2], 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        sys.exit("File not found: " + sys.argv[2])


if __name__ == '__main__':
    main()