import classes.bookclass  as book


title = input("What is the title? ")
qtpage = input("How many pages does the book have?")
author = input("Who is the author? ")
isbn = input("What is the ISBN? ")
location = input("Where is going to be? ")
qty = input("How many copies?")

newBook = book.Book(title, qtpage, isbn, author, location, qty)

book.insertABook(newBook)