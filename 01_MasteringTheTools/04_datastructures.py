from enum import Enum, auto

from typing import Tuple


class Month(Enum):
    JANUARY = auto()
    FEBRUARY = auto()
    MARCH = auto()
    APRIL = auto()
    MAY = auto()
    JUNE = auto()
    JULY = auto()
    AUGUST = auto()
    SEPTEMBER = auto()
    OCTOBER = auto()
    NOVEMBER = auto()
    DECEMBER = auto()


def is_birthday(month: Month):
    return month == Month.APRIL


def birthday_month_year() -> Tuple[Month, int]:
    return Month.APRIL, 1988


def main():
    x = 2.134e4
    l = [0, 1, 3]
    print(l[:1])  # [0]
    print(l[2:])  # [3]
    print(l[4:])  # []
    list_copy = l[:]
    list_copy[1] = -100
    print(l)  # [0, 1, 3]
    print(list_copy)  # [0, -100, 3]

    my_dict = {"one": 123, "two": 456, "three": 789}
    print(my_dict["one"])  # 123

    my_str = "hello"
    print(my_str)
    my_str2 = '''
    Hi this is also
    a string
    '''
    print(my_str2)
    my_str3 = "hello this is also a string"
    print("this" in my_str3)  # True
    print(my_str3[1:7])  # ello t
    print(my_str3[-3])  # i
    val = 3
    formatted_str = f"The value is {val}"
    print(formatted_str)  # The value is 3
    amount: int = 30000
    formatted_str2 = f"The amount is ${amount / 100:.2f}"
    print(formatted_str2)  # The amount is $300.00

    print(is_birthday(Month.APRIL))  # True
    my_month, my_year = birthday_month_year()
    print(my_month)  # Month.APRIL
    print(my_year)  # 1988

    x1: int = 5
    x2: float = 2.22
    x3 = x1 + x2
    print(x3)


if __name__ == "__main__":
    main()
