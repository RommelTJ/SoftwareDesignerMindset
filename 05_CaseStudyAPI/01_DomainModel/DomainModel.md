# Introduction and Domain Model

* Start with the data
* Spend time thinking about the domain model
  * This is also known as requirements engineering
* Hotel has: 
  * Rooms
  * Customers
  * Bookings
* Normally you would ask this in an interview with your client
* You have a hotel.db

```python
from dataclasses import dataclass
from datetime import date

@dataclass()
class Customer:
    id: int
    first_name: str
    last_name: str
    email_address: str

@dataclass()
class Room:
    id: int
    number: str
    size: int
    price: int

@dataclass()
class Booking:
    id: int
    from_date: date
    to_date: date
    customer: Customer
    room: Room
    price: int
```
