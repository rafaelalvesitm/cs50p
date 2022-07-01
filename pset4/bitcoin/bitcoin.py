import requests, sys

def main():
    # Read the command line arguments, check if the first argument is a number
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Missing command line argument")

    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")

    # Get the price rate of bitcoin from the coindesk api
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Could not connect to the API")

    # outputs the cost of n bitcoins in USD
    print(f"${float(sys.argv[1]) * float(r.json()['bpi']['USD']['rate_float']):,.4f}")


if __name__ == "__main__":
    main()
