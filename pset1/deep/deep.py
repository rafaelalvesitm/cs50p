def main():
    # Prompts the user for input
    input_string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    # Check for "42" or "forty-two" or "forty two"
    if "42" in input_string or "forty-two" in input_string or "forty two" in input_string:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()