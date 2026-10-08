def calculate(num1: float, num2: float, operation: str) -> float:
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1 - num2

    elif operation == "*":
        return num1 * num2

    elif operation == "%":
        if num2 == 0:
            raise ValueError("Modulo by zero is not allowed")
        else:
            return num1 % num2

    elif operation == "/":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            return num1 / num2

    else:
        raise ValueError(
            f"Invalid operation: '{operation}'. Choose from (+, -, *, %, /)."
        )