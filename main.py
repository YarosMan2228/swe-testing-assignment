"""
Quick-Calc: Command-line interface.

Usage:
    python main.py
"""

from calculator import Calculator


def display_menu():
    print("\n--- Quick-Calc ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear")
    print("6. Quit")


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    calc = Calculator()
    print(f"Current result: {calc.result}")

    while True:
        display_menu()
        choice = input("Select an operation (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice == "5":
            calc.clear()
            print(f"Cleared. Result: {calc.result}")
        elif choice in ("1", "2", "3", "4"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            try:
                if choice == "1":
                    result = calc.add(a, b)
                elif choice == "2":
                    result = calc.subtract(a, b)
                elif choice == "3":
                    result = calc.multiply(a, b)
                elif choice == "4":
                    result = calc.divide(a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
