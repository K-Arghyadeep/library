import library

# Create some books, authors, and members
book1 = library.Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0-395-07422-1")
book2 = library.Book("The Hobbit", "J.R.R. Tolkien", "978-0-00-712665-9")
book3 = library.Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "978-0-7475-2244-7")

author1 = library.Author("J.R.R. Tolkien", "British")
author2 = library.Author("J.K. Rowling", "British")

member1 = library.Member("Frodo Baggins", "The Shire", "123-456-7890")
member2 = library.Member("Harry Potter", "Hogwarts", "987-654-3210")

# Add books, authors, and members to the library
libraryy = library.Library()
libraryy.add_book(book1)
libraryy.add_book(book2)
libraryy.add_book(book3)

libraryy.add_author(author1)
libraryy.add_author(author2)

libraryy.add_member(member1)
libraryy.add_member(member2)

# Checkout and return books
libraryy.checkout_book(member1, book1)
libraryy.checkout_book(member2, book3)

libraryy.return_book(member1, book1)
libraryy.return_book(member2, book3)
