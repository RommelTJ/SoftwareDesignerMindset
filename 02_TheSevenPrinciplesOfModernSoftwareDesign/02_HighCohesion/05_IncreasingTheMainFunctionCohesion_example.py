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


def compute_rental_cost(vehicle: Vehicle, days: int, km: int) -> int:
    # Compute the final rental price
    return vehicle.price_per_km * km + vehicle.price_per_day * days


def main():
    vehicle_type = read_vehicle_type()
    vehicle = VEHICLE_DATA[vehicle_type]
    days = read_num_of_days()
    km = read_num_of_kms()
    rental_price = compute_rental_cost(vehicle, days, km)
    print(f"The total price of the rental is: ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
