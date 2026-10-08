from calculator import calculate
from lesson2 import calculate_total

def main():
    print("##################################################################################")
    print("Welcome PY-Calculator!\n")

    print("##################################################################################")
    try:
        price = float(input("Enter the price of the item: "))
        quantity = int(input("Enter the quntity of the item: "))
        total = calculate_total(price, quantity)
        print(f"\nTotal cost: {total}")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, %, /): ").strip()

        result = calculate(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError as e:
        # Handle both float conversion error and custom errors from calculator.py
        print(f"\nError: {e}")

        

    print("\nThank you for using PY-Calculator!")
    print("##################################################################################")




if __name__ == "__main__":
    main()