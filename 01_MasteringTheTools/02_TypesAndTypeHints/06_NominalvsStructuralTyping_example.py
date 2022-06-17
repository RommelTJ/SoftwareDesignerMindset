class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


def main():
    my_str = "hello"
    print(len(my_str))
    my_list = [23, 243, 234, 2]
    print(len(my_list))
    my_dict = {"one": 123, "two": 456, "three": 789}
    print(len(my_dict))
    my_book = Book("Rommel", "Clean Code", 464)
    print(len(my_book))


if __name__ == "__main__":
    main()
