from typing import List

from hotel.operations.interface import DataInterface, DataObject

from pydantic import BaseModel
from datetime import date


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date


def read_all_bookings(booking_interface: DataInterface) -> List[DataObject]:
    return booking_interface.read_all()


def read_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.read_by_id(booking_id)


def create_booking(data: BookingCreateData, booking_interface: DataInterface, room_interface: DataInterface) -> DataObject:
    # retrieve the room
    room = room_interface.read_by_id(data.room_id)

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates")
    booking_dict = data.dict()
    booking_dict["price"] = room["price"] * days

    return booking_interface.create(booking_dict)


def delete_booking(booking_id: int, booking_interface: DataInterface) -> DataObject:
    return booking_interface.delete(booking_id)
