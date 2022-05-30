import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


# class Vehicle(ABC):
#     @abstractmethod
#     def reserve(self, start_date: datetime, days: int) -> None:
#         """A vehicle can be reserved for renting"""

class Rentable(Protocol):
    def reserve(self, start_date: datetime, days: int) -> None:
        ...


class LicenseHolder(Protocol):
    def renew_license(self, new_license_date: datetime):
        ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    # If you comment it out, AttributeError: 'Car' object has no attribute 'reserve' (with Protocols)
    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing the license from {new_license_date}")



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


def reserve_now(rentable: Rentable):
    rentable.reserve(datetime.now(), 40)


def renew_license_now(license_holder: LicenseHolder):
    license_holder.renew_license(datetime.now())


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    # what = Vehicle()  # Can't instantiate abstract class Vehicle with abstract methods reserve
    # reserve_now(what)  # TypeError: reserve() missing 1 required positional argument: 'days'
    reserve_now(car)  # Reserving car Ford for 40 days at date 2022-05-30 10:34:05.422360.
    reserve_now(truck)  # Reserving truck DAF for 2 months at date 2022-05-30 10:34:05.422395 with trailer.
    renew_license_now(car)
    renew_license_now(truck)  # AttributeError: 'Truck' object has no attribute 'renew_license'


if __name__ == "__main__":
    main()
