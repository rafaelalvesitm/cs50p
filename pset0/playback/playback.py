def main():
    # Receive input from the user and store it in a variable
    user_input = input("Enter a string: ")
    # Replace each space with ...
    user_input = user_input.replace(" ", "...")
    # Print the string 
    print(user_input)


# Call main at the end of the program
if __name__ == "__main__":
    main()
