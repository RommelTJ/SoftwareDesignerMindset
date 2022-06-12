def main():
    l = [0, 1, 3]
    print(l[:1])  # [0]
    print(l[2:])  # [3]
    print(l[4:])  # []
    list_copy = l[:]
    list_copy[1] = -100
    print(l)  # [0, 1, 3]
    print(list_copy)  # [0, -100, 3]


if __name__ == "__main__":
    main()
