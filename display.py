def show_main_menu():
    """Prints the main interactive menu."""
    print("\n==================================")
    print("  PEMDAS & BITWISE CALCULATOR    ")
    print("==================================")
    print("1. PEMDAS Math Calculator (3 numbers)")
    print("2. Bitwise Logic Calculator")
    print("3. Exit")


def print_result(label, value):
    """Prints decimal results along with binary representations."""
    print(f"--> {label}: {value} (Binary: {bin(value)})")
