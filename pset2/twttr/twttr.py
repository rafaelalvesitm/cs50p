def main():
    # Prompts the uset for an input string
    string = input("Input: ")
    # Remove vowels from the string
    for character in string:
        if character in "aeiouAIUEO":
            string = string.replace(character, "")
    # Print the string
    print(string)

if __name__ == "__main__":
    main()
