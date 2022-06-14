import math
from dataclasses import dataclass
from datetime import datetime


class Vehicle:
    def reserve(self, start_date: datetime, days: int) -> None:
        """A vehicle can be reserved for renting"""


@dataclass
class Car(Vehicle):
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")


@dataclass
class Truck(Vehicle):
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(f"Reserving truck {self.model} for {months} months at date {start_date} with trailer.")


def reserve_now(vehicle: Vehicle):
    vehicle.reserve(datetime.now(), 40)


def main():
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)


if __name__ == "__main__":
    main()
