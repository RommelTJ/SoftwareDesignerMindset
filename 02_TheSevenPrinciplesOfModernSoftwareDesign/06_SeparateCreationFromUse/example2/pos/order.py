from dataclasses import dataclass, field
from typing import List

from pos.data import PaymentStatus


@dataclass()
class LineItem:
    item: str
    quantity: int
    price: int

    @property
    def total_price(self) -> int:
        return self.quantity * self.price


@dataclass()
class Order:
    items: List[LineItem] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: LineItem) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum(item.total_price for item in self.items)

    def set_status(self, status: PaymentStatus) -> None:
        self.status = status
