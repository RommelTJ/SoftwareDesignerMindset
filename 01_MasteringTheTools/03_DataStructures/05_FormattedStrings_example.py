def main():
    val = 3
    formatted_str = f"The value is {val}"
    print(formatted_str)  # The value is 3
    amount: int = 30000
    formatted_str2 = f"The amount is ${amount / 100:.2f}"
    print(formatted_str2)  # The amount is $300.00


if __name__ == "__main__":
    main()
