class Library:
    def __init__(self, books=None):
        self.books = books

    def add_book(self, book):
        self.books = self.books or []
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book_by_pamas(self, **kwargs):
        title = kwargs.get("title")
        author = kwargs.get("author")
        filter_books = []
        for book in self.books:
            if (title and book.title == title) or (author and book.author == author):
                filter_books.append(book)

        for i in range(len(filter_books)):
            filter_books[i] = filter_books[i].get_info()
        
        return filter_books

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def title(self):
        return self.title
    
    def author(self):
        return self.author
    
    def isAvailable(self):
        return self.availability
    
    def checkoutBook(self):
        self.availability = False

    def returnBook(self):
        self.availability = True

    def get_info(self):
	    return f"{self.title} {self.author}"


class User:
    def __init__(self, id, name, checkOutBooks):
        self.id = id
        self.name = name
        self.checkOutBooks = checkOutBooks

    def checkoutBook(self, book):
        if book in self.checkOutBooks:
            raise Exception("Book has already been taken by me.")
        self.checkOutBooks.append(book)

    def returnBook(self, book):
        if book not in self.checkOutBooks:
            raise Exception("Book has not been taken by me.")
        self.checkOutBooks.remove(book)

    def get_info(self):
	    return f"{self.name}"

class CheckOut:
    checkouts = {}

    @classmethod
    def checkOutBook(cls, book, user):
        if book in cls.checkouts:
            raise Exception("Book has already been checked out.")
        book.checkoutBook()
        user.checkoutBook(book)
        cls.checkouts[book] = user

    @classmethod
    def returnBook(cls, book, user):
        if book not in cls.checkouts:
            raise Exception("Book has not been checked out.")
        book.returnBook()
        user.returnBook(book)
        cls.checkouts.pop(book)

    @classmethod
    def get_all_checkout_books(cls):
        for key in cls.checkouts.keys():
            user_info = cls.checkouts[key].get_info()
            book_info = key.get_info()
            print(user_info, book_info)
        

book1 = Book("DBMS", "Morey", True)
book2 = Book("OS", "Alex", True)
book3 = Book("DSA", "Corey", True)

user1 = User(1, "Abhishek", [])
user2 = User(2, "Ria", [])


lib1 = Library()
lib1.add_book(book1)
lib1.add_book(book2)
lib1.add_book(book3)

CheckOut.checkOutBook(book1, user1)
# CheckOut.get_all_checkout_books()

# print(lib1.search_book_by_pamas(title="DBMS", author = "Alex"))

CheckOut.checkOutBook(book2, user1)
# CheckOut.get_all_checkout_books()

CheckOut.returnBook(book1, user1)
CheckOut.get_all_checkout_books()
