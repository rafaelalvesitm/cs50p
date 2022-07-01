import emoji

def main():
    # prompts the user for an input string
    input_string = input("Input: ")
    output = emoji.emojize(emoji.emojize(input_string), language='alias')
    print("Output: " + output)

if __name__ == "__main__":
    main()
