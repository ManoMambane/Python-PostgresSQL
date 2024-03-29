class Book:
    TYPES = ("hardcover", "paperback")


    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr___(self):
        return f"<Book {self.name}, {self.book_type}, it's weight is {self.weight}g>"
    
    def __str__(self):
        return f"Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)


#book = Book("Harry Potter", "hardcover", 1500)
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Mo", 500)

print(book)
print(light)