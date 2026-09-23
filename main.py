from pemdas_engine import solve_pemdas
from bitwise_engine import do_and, do_or, do_xor, do_not, do_left_shift, do_right_shift
from validator import is_valid_number, is_valid_operator
from display import show_main_menu, print_result


def run_app():
    while True:
        show_main_menu()
        choice = input("Select an option (1-3): ")

        if choice == "1":
            print("\n--- PEMDAS CALCULATOR ---")
            print("Format: Number1 Op1 Number2 Op2 Number3 (e.g., 2 + 3 * 4)")

            n1 = input("Enter first number: ")
            op1 = input("Enter first operator (+, -, *, /, ^): ")
            n2 = input("Enter second number: ")
            op2 = input("Enter second operator (+, -, *, /, ^): ")
            n3 = input("Enter third number: ")

            # Validate input
            if not (is_valid_number(n1) and is_valid_number(n2) and is_valid_number(n3)):
                print("Error: All inputs must be valid integers!")
                continue

            if not (is_valid_operator(op1) and is_valid_operator(op2)):
                print("Error: Invalid operator typed!")
                continue

            ans = solve_pemdas(int(n1), op1, int(n2), op2, int(n3))
            print(f"--> Result: {n1} {op1} {n2} {op2} {n3} = {ans}")

        elif choice == "2":
            print("\n--- BITWISE CALCULATOR ---")
            print("Operations: AND, OR, XOR, NOT, LEFT, RIGHT")
            op = input("Type operation: ").upper()

            val1 = input("Enter first number: ")
            if not is_valid_number(val1):
                print("Error: Must be a valid whole number!")
                continue

            num1 = int(val1)

            if op == "NOT":
                ans = do_not(num1)
                print_result("Result", ans)
            else:
                val2 = input("Enter second number: ")
                if not is_valid_number(val2):
                    print("Error: Must be a valid whole number!")
                    continue

                num2 = int(val2)

                if op == "AND":
                    ans = do_and(num1, num2)
                elif op == "OR":
                    ans = do_or(num1, num2)
                elif op == "XOR":
                    ans = do_xor(num1, num2)
                elif op == "LEFT":
                    ans = do_left_shift(num1, num2)
                elif op == "RIGHT":
                    ans = do_right_shift(num1, num2)
                else:
                    print("Error: Unknown bitwise operation!")
                    continue

                print_result("Result", ans)

        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_app()
