def main():
    # Prompts the user for input
    input_string = input("Greeting: ")
    print(f"${value(input_string)}")

def value(greeting):
    # If hello in input_string output 0$ else if "h" is first letter output 20$ else output 100$
    if "hello" in greeting.lower():
        return 0
    elif greeting[0].lower() == "h":
        return 20 
    else:
        return 100

if __name__ == "__main__":
    main()