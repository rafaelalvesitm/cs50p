def main():
    # Prompts the uset for an input string
    string = input("Input: ")
    # Remove vowels from the string
    string = shorten(string)
    # Print the string
    print(string)


def shorten(word):
    # Loop through the word and remove vowels in lowercase or uppercase
    for character in word:
        if character in "aeiouAEIOU":
            word = word.replace(character, "")
    return word


if __name__ == "__main__":
    main()
