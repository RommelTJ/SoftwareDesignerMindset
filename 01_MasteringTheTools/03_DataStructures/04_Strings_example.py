def main():
    my_str = "hello"
    print(my_str)
    my_str2 = '''
    Hi this is also
    a string
    '''
    print(my_str2)
    my_str3 = "hello this is also a string"
    print("this" in my_str3)  # True
    print(my_str3[1:7])  # ello t
    print(my_str3[-3])  # i
    val = 3
    formatted_str = f"The value is {val}"
    print(formatted_str)  # The value is 3
    amount: int = 30000
    formatted_str2 = f"The amount is ${amount / 100:.2f}"
    print(formatted_str2)  # The amount is $300.00


if __name__ == "__main__":
    main()
