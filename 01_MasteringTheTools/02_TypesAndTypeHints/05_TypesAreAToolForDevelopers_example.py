from typing import Callable


IntFunction = Callable[[int], int]


def compute_stats(users, plans, products):
    # Some complicate code
    pass


def multiply_by_two(x: float) -> float:
    return x * 2.0


def add_three(x: int) -> int:
    return x + 3


def main():
    # my_var = add_three(5)
    my_var: IntFunction = add_three  # my_var is a callable now.
    print(my_var)

    my_var: IntFunction = multiply_by_two  # Wrong type, but Python interpreter won't stop you.
    print(my_var(5))


if __name__ == "__main__":
    main()
