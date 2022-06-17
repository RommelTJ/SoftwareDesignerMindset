from enum import Enum, auto


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


def main():
    print(is_birthday(Month.APRIL))  # True


if __name__ == "__main__":
    main()
