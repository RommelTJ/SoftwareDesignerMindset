from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol, List


class Pricing(Protocol):
    def get_total_price(self) -> int:
        ...


@dataclass
class PricePerDay:
    price_per_day: int
    num_of_days: int

    def get_total_price(self) -> int:
        return self.price_per_day * self.num_of_days


@dataclass
class PricePerKm:
    price_per_km: int
    num_of_kms: int

    def get_total_price(self) -> int:
        return self.price_per_km * self.num_of_kms


@dataclass
class PricePerMonth:
    price_per_month: int
    num_of_months: int

    def get_total_price(self) -> int:
        return self.price_per_month * self.num_of_months


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    pricing: List[Pricing] = field(default_factory=list)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 200


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool
    pricing: List[Pricing] = field(default_factory=list)


def main():
    pass


if __name__ == "__main__":
    main()
