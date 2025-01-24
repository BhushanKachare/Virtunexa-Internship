import random

def roll_dice(sides):
    """Simulates rolling a dice with a given number of sides."""
    return random.randint(1, sides)

def dice_simulator():
    print("Welcome to the Dice Simulator!")

    while True:
        print("\nOptions:")
        print("1. Roll a D6 (6-sided dice)")
        print("2. Roll a D20 (20-sided dice)")
        print("3. Roll a custom dice")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '4':
            print("Exiting Dice Simulator. Goodbye!")
            break

        if choice == '1':
            print(f"You rolled a D6 and got: {roll_dice(6)}")
        elif choice == '2':
            print(f"You rolled a D20 and got: {roll_dice(20)}")
        elif choice == '3':
            try:
                sides = int(input("Enter the number of sides for your dice: "))
                if sides < 2:
                    print("A dice must have at least 2 sides. Please try again.")
                else:
                    print(f"You rolled a D{sides} and got: {roll_dice(sides)}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    dice_simulator()
