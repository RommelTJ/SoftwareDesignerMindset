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


if __name__ == "__main__":
    main()
