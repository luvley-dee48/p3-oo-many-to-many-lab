class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string.")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")
        new_contract = Contract(author=self, book=book, date=date, royalties=royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string.")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str) or not date:
            raise Exception("Date must be a non-empty string.")
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __eq__(self, other):
        if isinstance(other, Contract):
            return (self.author == other.author and
                    self.book == other.book and
                    self.date == other.date and
                    self.royalties == other.royalties)
        return False

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"
