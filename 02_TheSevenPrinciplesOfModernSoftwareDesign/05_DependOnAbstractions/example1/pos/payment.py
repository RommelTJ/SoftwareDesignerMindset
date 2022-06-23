from typing import Callable

from pos.data import PaymentStatus
from pos.order import Order


AuthorizeFunction = Callable[[], bool]


class PaymentProcessor:
    def __init__(self, authorize: AuthorizeFunction):
        self.authorize = authorize

    def pay_debit(self, order: Order) -> None:
        if not self.authorize():
            raise Exception("Not authorized")
        print(f"Processing debit payment for amount: ${(order.total_price / 100):.2f}.")
        order.status = PaymentStatus.PAID

    def pay_credit(self, order: Order, security_code: str) -> None:
        if not self.authorize():
            raise Exception("Not authorized")
        print(f"Processing credit payment for amount: ${(order.total_price / 100):.2f}.")
        print(f"Verifying security code: {security_code}")
        order.status = PaymentStatus.PAID
