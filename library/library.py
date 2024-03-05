class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"Author: {self.name} from {self.nationality}"

class Member:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"Member: {self.name} from {self.address}"

class Library:
    def __init__(self):
        self.books = []
        self.authors = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_author(self, author):
        self.authors.append(author)

    def add_member(self, member):
        self.members.append(member)

    def checkout_book(self, member, book):
        if book not in self.books:
            print(f"Book {book.title} is not available")
            return

        if member not in self.members:
            print(f"Member {member.name} is not registered")
            return

        book.is_available = False
        print(f"Book {book.title} has been checked out to {member.name}")

    def return_book(self, member, book):
        if book not in self.books:
            print(f"Book {book.title} is not available")
            return

        if member not in self.members:
            print(f"Member {member.name} is not registered")
            return

        if book.is_available:
            print(f"Book {book.title} is already available")
            return

        book.is_available = True
        print(f"Book {book.title} has been returned by {member.name}")