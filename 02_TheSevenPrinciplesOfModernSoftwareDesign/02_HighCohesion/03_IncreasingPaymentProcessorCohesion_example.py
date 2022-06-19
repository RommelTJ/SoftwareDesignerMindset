from enum import Enum, auto
from typing import List


class PaymentStatus(Enum):
    """Payment status"""
    OPEN = auto()
    PAID = auto()


class Order:
    def __init__(self):
        self.items: List[str] = []
        self.quantities: List[int] = []
        self.prices: List[int] = []
        self.status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_status(self, status: PaymentStatus) -> None:
        self.status = status


class PaymentProcessor:

    def pay_debit(self, order: Order, security_code: str) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(PaymentStatus.PAID)

    def pay_credit(self, order: Order, security_code: str) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status(PaymentStatus.PAID)


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    processor = PaymentProcessor()
    processor.pay_debit(order, "0372846")


if __name__ == "__main__":
    main()
