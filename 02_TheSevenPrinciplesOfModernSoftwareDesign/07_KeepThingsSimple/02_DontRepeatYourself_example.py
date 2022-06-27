from typing import List


def read_choice(question: str, choices: List[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def read_vehicle_type():
    vehicle_types = ["vw", "bmw", "tesla"]
    return read_choice("What type of vehicle would you like to rent", vehicle_types)


def read_vehicle_color():
    vehicle_colors = ["black", "red", "blue"]
    return read_choice("What color vehicle would you like to rent", vehicle_colors)


def read_rent_days():
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(f"How many days would you like to rent the vehicle? ")
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive():
    """Reads the number of kms to drive from the user."""
    kms = 0
    while kms < 1:
        km_str = input(f"How many kms would you like to drive? ")
        try:
            kms = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return kms


def main() -> None:
    vehicle_type = read_vehicle_type()
    vehicle_color = read_vehicle_color()
    days = read_rent_days()
    kms = read_kms_to_drive()
    print(
        f"You rented a {vehicle_type} vehicle, color {vehicle_color}, for {days} days",
        f"and you're allowed to drive {kms} kilometers."
    )


if __name__ == "__main__":
    main()
