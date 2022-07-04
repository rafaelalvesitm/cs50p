import sys, tabulate, csv

from PIL import Image, ImageOps


def main():
    # Check for 2 command line arguments and split filename to be
    try:
        before, before_extension = sys.argv[1].lower().split(".")
        after, after_extension = sys.argv[2].lower().split(".")
    except:
        sys.exit("Usage: python3 shirt.py <filename.csv> <filename.csv>")

    if (
        len(sys.argv) != 3
        or before_extension not in ["jpg", "png", "jpeg"]
        or after_extension not in ["jpg", "png", "jpeg"]
        or before_extension != after_extension
    ):
        sys.exit(
            "Usage: python shirt.py <before.ext> <after.ext> (before and after can be png, jpg, jpeg and must be the same extension"
        )

    # Read the input image
    try:
        before_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found: " + sys.argv[1])

    # Open shirt image and resize image
    shirt = Image.open("shirt.png")
    size = shirt.size
    # Resize image to match the size of the before image
    before_image = ImageOps.fit(before_image, size)
    # Create a new image with the same size as the before image
    before_image.paste(shirt, (0, 0), shirt)
    before_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
