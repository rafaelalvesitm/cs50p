import sys

def main():
    grocery_list = dict()
    while True:
        # Prompt the user for one item, if ctrl+d pressed break the loop
        try:
            item = input().upper()
        except EOFError:
            break
        # Add the item to the grocery list.
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    # order a the grocery list dictionary
    try:
        grocery_list = dict(sorted(grocery_list.items(),  key = lambda item: item[0]))
    except:
        sys.exit()

    # print the grocery list
    for item, value in grocery_list.items():
        print(f"{value} {item}")

if __name__ == "__main__":
    main()
