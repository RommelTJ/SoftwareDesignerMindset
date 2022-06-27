from typing import List, Dict

from pos.order import LineItem, Order
from pos.payment import CreditPaymentProcessor, PaypalPaymentProcessor, DebitPaymentProcessor, AuthorizeFunction
from pos.authorization import authorize_sms, authorize_google


AUTHORIZERS: Dict[str, AuthorizeFunction] = {
    "google": authorize_google,
    "sms": authorize_sms
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


def main():
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB Cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    # select the payment method
    payment_processor_choice = read_choice("How would you like to pay?", ["paypal", "credit", "debit"])

    if payment_processor_choice == "paypal":
        email_address = input("Enter your email address: ")
        processor = PaypalPaymentProcessor(email_address)
    elif payment_processor_choice == "credit":
        security_code = input("Enter the security code: ")
        processor = CreditPaymentProcessor(security_code)
    else:
        processor = DebitPaymentProcessor()

    authorizer = read_authorizer()
    processor.pay(order, authorizer)


if __name__ == "__main__":
    main()
