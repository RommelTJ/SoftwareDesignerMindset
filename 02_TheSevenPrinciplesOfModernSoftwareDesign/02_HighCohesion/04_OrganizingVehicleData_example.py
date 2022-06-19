from dataclasses import dataclass


@dataclass()
class Vehicle:
    price_per_km: int
    price_per_day: int


VEHICLE_DATA = {
    "vw": Vehicle(price_per_km=30, price_per_day=6000),
    "bmw": Vehicle(price_per_km=35, price_per_day=8500),
    "ford": Vehicle(price_per_km=25, price_per_day=12000),
}


def read_vehicle_type() -> str:
    vehicle_type = ""
    while vehicle_type not in VEHICLE_DATA:
        vehicle_type = input("What type of vehicle would you like to rent (vw, bmw, or ford)? ")
    return vehicle_type


def read_num_of_days() -> int:
    days = 0
    while days < 1:
        days_str = input("How many days would you like to rent the vehicle? ")
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_num_of_kms() -> int:
    km = 0
    while km < 1:
        km_str = input("How many kms would you like to drive? ")
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Subtract the base number of kms
    km = max(km - 100, 0)  # First 100 kms are free.
    return km


def main():
    vehicle_type = read_vehicle_type()
    days = read_num_of_days()
    km = read_num_of_kms()

    # Compute the final rental price
    rental_price = 0
    if vehicle_type == "vw":
        rental_price = price_per_km_vw * km + price_per_day_vw * days
    elif vehicle_type == "bmw":
        rental_price = price_per_km_bmw * km + price_per_day_bmw * days
    elif vehicle_type == "ford":
        rental_price = price_per_km_ford * km + price_per_day_ford * days
    else:
        print("Error")

    # Print the result
    print(f"The total price of the rental is: ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
