from lesson2 import square, is_even
print("******************************************************************")
def main():
    print("Welcome to the Python Engineering Demo!\n")

    # Chanllenge 1 
    user_input = int(input("Enter a number to square: "))
    squared_num = square(user_input)
    print(f"The square of {user_input}: {squared_num}")

    print("--------------------------------------------------")
    # Chanllenge 2
    num = int(input("Enter a number to check if it's even or odd: "))
    check_num = is_even(num)
    print(f"The number {num} is even: {check_num}")

    print("--------------------------------------------------")

    print("*************************************************************************")


if __name__ == "__main__":
    main()