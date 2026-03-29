class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book")
        if not isinstance(date, str) or len(date.strip()) == 0:
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

    # 👇 ADD THIS METHOD
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]