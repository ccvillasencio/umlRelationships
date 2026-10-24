class Book:
    def __init__(self, title: str):
        self.title = title


class Library:
    def __init__(self, books=None):
        # The Library accepts already-existing Book objects.
        self.books = books if books is not None else []


# --- Running the code ---
book1 = Book("The Hobbit")
book2 = Book("1984")

my_library = Library([book1, book2])

print("Library populated with:",
      [book.title for book in my_library.books])

print("\nDeleting the library...")
del my_library

print("\nChecking book accessibility:")
print("Book 1 still exists:", book1.title)
print("Book 2 still exists:", book2.title)
