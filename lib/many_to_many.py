class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        unique_books = []
        for contract in self.contracts():
            if contract.book not in unique_books:
                unique_books.append(contract.book)
        return unique_books

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        unique_authors = []
        for contract in self.contracts():
            if contract.author not in unique_authors:
                unique_authors.append(contract.author)
        return unique_authors


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book")
        if not isinstance(date, str) or not date.strip():
            raise ValueError("date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise ValueError("royalties must be an integer between 0 and 100")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]