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


def birthday_month_year() -> Tuple[Month, int]:
    return Month.APRIL, 1988


def main():
    my_month, my_year = birthday_month_year()
    print(my_month)  # Month.APRIL
    print(my_year)  # 1988


if __name__ == "__main__":
    main()
