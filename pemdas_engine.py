def solve_two_numbers(num1, op, num2):
    """Solves a basic math operation between two numbers."""
    if op == "^":
        return num1 ** num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    return 0


def solve_pemdas(num1, op1, num2, op2, num3):
    """
    Solves a 3-number problem following PEMDAS manually.
    Example: 2 + 3 * 4 -> solves 3 * 4 first, then adds 2.
    """
    # Check if second operation has higher precedence (*, /, ^ before +, -)
    if op2 in ["*", "/", "^"] and op1 in ["+", "-"]:
        # Step 1: Solve right side first
        right_result = solve_two_numbers(num2, op2, num3)
        # Step 2: Solve left side with the right result
        return solve_two_numbers(num1, op1, right_result)
    else:
        # Step 1: Solve left side first (standard left-to-right)
        left_result = solve_two_numbers(num1, op1, num2)
        # Step 2: Solve right side
        return solve_two_numbers(left_result, op2, num3)
