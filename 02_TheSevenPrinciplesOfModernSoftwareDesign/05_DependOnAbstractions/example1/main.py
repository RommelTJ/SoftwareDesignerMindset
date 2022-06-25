from pos.order import LineItem, Order
from pos.payment import CreditPaymentProcessor
from pos.authorization import authorize_sms


def main():
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB Cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")
    processor = CreditPaymentProcessor("123456")
    processor.pay(order, authorize_sms)


if __name__ == "__main__":
    main()
