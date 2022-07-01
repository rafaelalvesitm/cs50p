import random

def main():
    # Prompts the user for a level of difficulty.
    while True:
        try:
            level = int(input("Level: "))
        except:
            continue
        if level > 0:
                break

    # Generates a random number between 1 and the level.
    random_number = random.randint(1, level)

    # Prompts the user for a guess.
    while True:
        try:
            guess = int(input("Guess: "))
        except:
            continue
        if guess > 0:
            # Checks if the guess is correct.
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too small!")
            else:
                print("Just right!")
                break




if __name__ == "__main__":
    main()
