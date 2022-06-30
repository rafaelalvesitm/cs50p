def main():
    # Prompts the user for input
    input_string = input("Greeting: ").lower()
    # If hello in input_string output 0$ else if "h" is first letter output 20$ else output 100$
    if "hello" in input_string:
        print("$0")
    elif input_string[0] in "h":
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()