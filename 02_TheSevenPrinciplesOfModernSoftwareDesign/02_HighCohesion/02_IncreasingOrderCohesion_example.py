from typing import List


class Order:
    def __init__(self):
        self.items: List[str] = []
        self.quantities: List[int] = []
        self.prices: List[int] = []
        self.status: str = "open"

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def set_status(self, status: str) -> None:
        self.status = status


class PaymentProcessor:

    def pay(self, order: Order, payment_type: str, security_code: str) -> None:
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_status("paid")
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            order.set_status("paid")
        else:
            raise ValueError(f"Unknown payment type: {payment_type}")


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    processor = PaymentProcessor()
    processor.pay(order, "debit", "0372846")


if __name__ == "__main__":
    main()
