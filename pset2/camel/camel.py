def main():
    # Ask the user for a camel case string
    camel_case = input("camelCase: ")
    # change camel case to snake case
    for character in camel_case:
        if character.isupper():
            print(f"_{character.lower()}", end="")
        else:
            print(character, end="")
    print()


if __name__ == "__main__":
    main()