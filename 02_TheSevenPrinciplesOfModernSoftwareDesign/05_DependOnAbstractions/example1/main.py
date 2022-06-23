from pos.order import LineItem, Order
from pos.payment import PaymentProcessor
from pos.authorization import authorize_sms


def main():
    order = Order()
    order.add_item(LineItem("Keyboard", 1, 5000))
    order.add_item(LineItem("SSD", 1, 15000))
    order.add_item(LineItem("USB Cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")
    processor = PaymentProcessor(authorize_sms)
    processor.pay_credit(order, "123456")


if __name__ == "__main__":
    main()
