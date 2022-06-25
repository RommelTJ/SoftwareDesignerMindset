from dataclasses import dataclass
from typing import Callable, Protocol

from pos.data import PaymentStatus

AuthorizeFunction = Callable[[], bool]


class Payable(Protocol):
    @property
    def total_price(self) -> int:
        ...

    def set_status(self, status: PaymentStatus) -> None:
        ...


class PaymentProcessor(Protocol):
    def pay(self, payable: Payable, authorize: AuthorizeFunction):
        ...


class DebitPaymentProcessor:
    def pay(self, payable: Payable, authorize: AuthorizeFunction):
        if not authorize():
            raise Exception("Not authorized")
        print(f"Processing debit payment for amount: ${(payable.total_price / 100):.2f}.")
        payable.set_status(PaymentStatus.PAID)


@dataclass
class CreditPaymentProcessor:
    security_code: str

    def pay(self, payable: Payable, authorize: AuthorizeFunction):
        if not authorize():
            raise Exception("Not authorized")
        print(f"Processing credit payment for amount: ${(payable.total_price / 100):.2f}.")
        print(f"Verifying security code: {self.security_code}")
        payable.set_status(PaymentStatus.PAID)


@dataclass
class PaypalPaymentProcessor:
    email_address: str

    def pay(self, payable: Payable, authorize: AuthorizeFunction):
        if not authorize():
            raise Exception("Not authorized")
        print(f"Processing Paypal payment for amount: ${(payable.total_price / 100):.2f}.")
        print(f"Using email address: {self.email_address}")
        payable.set_status(PaymentStatus.PAID)
