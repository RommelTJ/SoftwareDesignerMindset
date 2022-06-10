from typing import Callable


IntFunction = Callable[[int], int]


class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

# def compute_stats(users, plans, products):
#     # Some complicate code
#     pass
#
#
# def multiply_by_two(x: float) -> float:
#     return x * 2.0
#
#
# def add_three(x: int) -> int:
#     return x + 3


def main():
    # my_var = "hello"
    # my_var = 5  # You can re-assign because my_var doesn't have a type.

    # my_var = 5 + "hello"  # Unsupported operand + for int and str.
    # my_var = str(5) + "hello"  # Ok since we converted explicitly.

    # my_var = add_three(5)
    # my_var: IntFunction = add_three  # my_var is a callable now.

    # my_var: IntFunction = multiply_by_two  # Wrong type, but Python interpreter won't stop you.
    # print(my_var(5))

    my_str = "hello"
    print(len(my_str))
    my_list = [23, 243, 234, 2]
    print(len(my_list))
    my_dict = {"one": 123, "two": 456, "three": 789}
    print(len(my_dict))
    my_book = Book("Rommel", "Clean Code", 464)
    print(len(my_book))


if __name__ == "__main__":
    main()
