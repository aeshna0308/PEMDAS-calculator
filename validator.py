def is_valid_number(text):
    """Checks if input is a valid whole integer."""
    try:
        int(text)
        return True
    except ValueError:
        return False


def is_valid_operator(op):
    """Checks if an operator string is valid for PEMDAS."""
    return op in ["+", "-", "*", "/", "^"]
