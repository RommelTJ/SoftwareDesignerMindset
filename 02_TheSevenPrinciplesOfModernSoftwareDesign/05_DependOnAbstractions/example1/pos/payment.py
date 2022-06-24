from typing import Callable, Protocol

from pos.data import PaymentStatus

AuthorizeFunction = Callable[[], bool]


class Payable(Protocol):
    @property
    def total_price(self) -> int:
        ...

    def set_status(self, status: PaymentStatus) -> None:
        ...


class PaymentProcessor:
    def __init__(self, authorize: AuthorizeFunction):
        self.authorize = authorize

    def pay_debit(self, payable: Payable) -> None:
        if not self.authorize():
            raise Exception("Not authorized")
        print(f"Processing debit payment for amount: ${(payable.total_price / 100):.2f}.")
        payable.set_status(PaymentStatus.PAID)

    def pay_credit(self, payable: Payable, security_code: str) -> None:
        if not self.authorize():
            raise Exception("Not authorized")
        print(f"Processing credit payment for amount: ${(payable.total_price / 100):.2f}.")
        print(f"Verifying security code: {security_code}")
        payable.set_status(PaymentStatus.PAID)
