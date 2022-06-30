menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0
    while True:
        # Prompt the user for their order
        try:
            order = input("Item: ")
        except EOFError:
            print()
            break
        # If the order isin the menu add to the total
        if order.title() in menu:
            total = menu[order.title()] + total
        print("Total: $%.2f" % total)


if __name__ == "__main__":
    main()
