import sys
from typing import Optional, List


def read_choice(question: str, choices: List[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def read_int(question: str, min_val: int = 0, max_val: int = sys.maxsize, forbidden_values: List[int] = None) -> int:
    value: Optional[int] = None
    if not forbidden_values:
        forbidden_values = []
    while (
        value is None
        or value < min_val
        or value > max_val
        or value in forbidden_values
    ):
        days_str = input(f"{question} ")
        try:
            value = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return value


def main():
    vehicle_type = read_choice("What type of vehicle would you like to rent", ["vw", "bmw", "tesla"])
    vehicle_color = read_choice("What color vehicle would you like to rent", ["black", "red", "blue"])
    days = read_int("How many days would you like to rent the vehicle?")
    kms = read_int("How many kms do you need to drive?", max_val=200)
    print(
        f"You rented a {vehicle_type} vehicle, color {vehicle_color}, for {days} days",
        f"and you're allowed to drive {kms} kilometers."
    )


if __name__ == "__main__":
    main()
