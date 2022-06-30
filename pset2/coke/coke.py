def main():
    # Define the amout due in the machine and print its value
    amout_due = 50
    print(f"Amount due: {amout_due}")

    # Loop while there still an amout due
    while amout_due > 0:
        # Asks the user for a coin
        coin = input("Insert coin: ")
        # If the coin is a valid coin, subtract the coin from the amout value and if negative print the change and exit the loop
        if coin == "5" or coin == "10" or coin == "25":
            amout_due -= int(coin)
            if amout_due <= 0:
                print(f"Change owed: {-amout_due}")
                break
            
        print(f"Amout due: {amout_due}")


if __name__ == "__main__":
    main()
