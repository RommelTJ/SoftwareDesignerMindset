import math
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Vehicle(Protocol):
    def reserve(self, start_date: datetime, days: int) -> None:
        """A vehicle can be reserved for renting"""
        ...

    def renew_license(self, new_license_date: datetime):
        ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")


@dataclass
class Truck:
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(f"Reserving truck {self.model} for {months} months at date {start_date} with trailer.")

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing the license from {new_license_date}")


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def renew_license_now(vehicle: Vehicle):
    vehicle.renew_license(datetime.now())


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)
    renew_license_now(truck)
    # renew_license_now(car) # AttributeError: 'Car' object has no attribute 'renew_license'


if __name__ == "__main__":
    main()
