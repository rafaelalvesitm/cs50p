def main():
    # Ask the user for an arithmetic expression in the format x y z:
    x, y, z = input("Expression: ").lower().split(" ")
    # Return the result of the expression for each of the four operator (+, -, *, or /)
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))


if __name__ == "__main__":
    main()