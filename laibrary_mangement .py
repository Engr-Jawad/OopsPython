class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    return f"You have successfully borrowed '{title}'."
                else:
                    return f"Sorry, '{title}' is currently not available."
        return f"Book '{title}' not found in the library."

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    return f"Thank you for returning '{title}'."
                else:
                    return f"'{title}' was not borrowed."
        return f"Book '{title}' not found in the library."

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(book)


# Example usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    library.add_book(book1)
    library.add_book(book2)

    library.display_books()

    print(library.borrow_book("1984"))
    print(library.borrow_book("1984"))  # Trying to borrow again

    library.display_books()

    print(library.return_book("1984"))
    library.display_books()
