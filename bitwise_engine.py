def do_and(a, b):
    return a & b


def do_or(a, b):
    return a | b


def do_xor(a, b):
    return a ^ b


def do_not(a):
    return ~a


def do_left_shift(a, shifts):
    return a << shifts


def do_right_shift(a, shifts):
    return a >> shifts
