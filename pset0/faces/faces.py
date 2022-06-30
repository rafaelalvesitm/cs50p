def main():
    # Prompts the user for a string
    user_input = input("Enter a string: ")
    # Converts the string
    user_input = convert(user_input)
    # Prints the string
    print(user_input)

def convert(string):
    # Replace :) with a smiley face
    string = string.replace(":)", "🙂")
    # Replace :( with a frowny face
    string = string.replace(":(", "🙁")
    return string

if __name__ == '__main__':
    main()