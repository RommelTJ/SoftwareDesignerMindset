from typing import List, Dict, Callable

from pos.authorization import authorize_sms, authorize_google
from pos.order import LineItem, Order
from pos.payment import (
    CreditPaymentProcessor,
    PaypalPaymentProcessor,
    DebitPaymentProcessor,
    AuthorizeFunction,
    PaymentProcessor
)

AUTHORIZERS: Dict[str, AuthorizeFunction] = {
    "google": authorize_google,
    "sms": authorize_sms
}


def create_paypal_payment_processor() -> PaymentProcessor:
    email_address = input("Enter your email address: ")
    return PaypalPaymentProcessor(email_address)


def create_debit_payment_processor() -> PaymentProcessor:
    return DebitPaymentProcessor()


def create_credit_payment_processor() -> PaymentProcessor:
    security_code = input("Enter the security code: ")
    return CreditPaymentProcessor(security_code)


PROCESSORS: Dict[str, Callable[[], PaymentProcessor]] = {
    "paypal": create_paypal_payment_processor,
    "debit": create_debit_payment_processor,
    "credit": create_credit_payment_processor
}


def read_choice(question: str, choices: List[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


def read_authorizer() -> AuthorizeFunction:
    # select the authentication method
    auth_choice = read_choice("Choose your authentication method", list(AUTHORIZERS.keys()))
    return AUTHORIZERS[auth_choice]


def read_payment_processor() -> PaymentProcessor:
    payment_processor_choice = read_choice("How would you like to pay?", ["paypal", "credit", "debit"])
    return PROCESSORS[payment_processor_choice]()


def main():
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB Cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    processor = read_payment_processor()
    authorizer = read_authorizer()
    processor.pay(order, authorizer)


if __name__ == "__main__":
    main()
