
C = 300000000 # Speed of light in meters per second

def main():
    # Prompts the user for a mass in kilograms
    m = int(input("m: "))
    # Calculate the energy in Joules based on E=mC^2
    energy = m * C * C 
    print("E: " + str(energy))

if __name__ == '__main__':
    main()