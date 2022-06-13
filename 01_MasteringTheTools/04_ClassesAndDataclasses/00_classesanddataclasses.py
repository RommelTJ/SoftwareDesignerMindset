import random
import string
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto

from typing import List


def generate_vehicle_license() -> str:
    """Helper function for generating a vehicle license number."""
    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


def default_accessories():
    return [Accessory.AIRCO, Accessory.NAVIGATION]


# @dataclass(frozen=True)
@dataclass()
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str = field(default_factory=generate_vehicle_license, init=False)
    # license_plate: str = field(init=False)
    accessories: List[Accessory] = field(default_factory=default_accessories)  # Better
    # accessories: List[Accessory] = field(default_factory=lambda: [Accessory.AIRCO, Accessory.NAVIGATION])
    fuel_type: FuelType = FuelType.ELECTRIC

    # def __post_init__(self):
    #     self.license_plate = generate_vehicle_license()
    #     if self.brand == "Tesla":
    #         self.license_plate += "-t"

    def reserve(self, date: datetime):
        print(f"Vehicle is reserved for {date}.")


def main() -> None:
    """Create some vehicles and print their details"""
    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL
        ]
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white"
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        fuel_type=FuelType.PETROL,
        # license_plate="FAKELICENSE",  # TypeError: __init__() got an unexpected keyword argument 'license_plate'
        accessories=[
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL
        ]
    )

    print(tesla)
    print(volkswagen)
    print(bmw)

    bmw.reserve(datetime.now())
    # bmw.brand = "Tesla"  # dataclasses.FrozenInstanceError: cannot assign to field 'brand'


if __name__ == "__main__":
    main()
