def main():
    # my_var = 5 + "hello"  # Unsupported operand + for int and str.
    my_var = str(5) + "hello"  # Ok since we converted explicitly.
    print(my_var)


if __name__ == "__main__":
    main()
