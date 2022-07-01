import inflect

def main():
    name_list = list()
    while True:
        # Prompt the user for one name, if ctrl+d pressed break the loop
        try:
            item = input("Name: ").title()
        except EOFError:
            break
        
        # Add the name to the name list.
        name_list.append(item)

    print()
    output = inflect.engine().join(name_list)
    print("Adieu, adieu, to " + output)

if __name__ == "__main__":
    main()
