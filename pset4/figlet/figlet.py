import random
import sys

from pyfiglet import Figlet


def main():
    # Get a lista of avaliable fonts
    figlet = Figlet()
    list_fonts = figlet.getFonts()

    # Checks for the lenght of the command line arguments
    if len(sys.argv) > 3:
        sys.exit("Invalid Usage")
    elif len(sys.argv) == 3:
        # Checks if the third argument is a valid font
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in list_fonts:
                font = sys.argv[2]
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 2:
        sys.exit("Invalid Usage")
    else:
        # Choose a random font
        font = random.choice(list_fonts)

    # Ask the user for an input string
    input_string = input("Input: ")
    # Set the font to the chosen font
    figlet.setFont(font=font)
    # Prints the output
    print("Output: " + figlet.renderText(input_string))


if __name__ == "__main__":
    main()
