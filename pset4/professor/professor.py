import random


def main():
    # Get a level of difficulty.
    level = get_level()
    # get a score
    score = 0
    # Generate 10 math problems
    for i in range(10):
        # generate a random numbers
        x = generate_integer(level)
        y = generate_integer(level)
        # Check if the user's answer is correct.
        correct = False
        # Take 3 guesses at maximum
        for i in range(3):
            # If wrong input or guess print EEE
            try:
                guess = int(input(f"{x} + {y} = "))
            except:
                print("EEE")
                continue
            if guess != x + y:
                print("EEE")
            # if correct increase the score, signal correct and break the loop
            else:
                correct = True
                score += 1
                break
        # if not corret at the end show the answer
        if not correct:
            print(f"{x} + {y} = {x + y}")
    # At the end of the game show the score
    print(f"Score: {score}")


def get_level():
    # Prompts the user for a level of difficulty.
    while True:
        try:
            level = int(input("Level (1-3): "))
        except:
            continue
        if level in [1, 2, 3]:
            break
    return level


def generate_integer(level):
    # generate a random non negative integer with level digits
    if level not in [1, 2, 3]:
        raise ValueError("level must be 1, 2, or 3")
    if level == 1:
        return random.randint(0, 10)
    elif level == 2:
        return random.randint(10, 100)
    elif level == 3:
        return random.randint(100, 1000)


if __name__ == "__main__":
    main()
