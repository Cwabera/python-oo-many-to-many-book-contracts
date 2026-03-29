# Many-to-Many Relationship Lab: Authors, Books, and Contracts

## Overview

In this lab, we implement a **many-to-many relationship** in Python using object-oriented programming (OOP).

The system models how **authors collaborate on books through contracts**:

* An **Author** can have many **Books**
* A **Book** can have many **Authors**
* The relationship is managed through a **Contract**

This mimics real-world publishing scenarios where multiple authors contribute to multiple books.

---

## Project Structure

```
python-oo-many-to-many/
│
├── lib/
│   └── many_to_many.py
│
├── testing/
│   ├── conftest.py
│   └── test_many_to_many.py
│
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

---

## Setup Instructions

### 1. Install dependencies

If you're using pipenv:

```bash
pipenv install
```

### 2. Activate virtual environment

```bash
pipenv shell
```

---

## Running Tests

To verify your implementation:

```bash
pytest
```

Or:

```bash
pipenv run pytest
```

---

## Models

### Author

Represents a writer.

#### Attributes:

`name` (string)

#### Methods:

`contracts()` → returns all contracts for the author
`books()` → returns unique books the author has worked on
`sign_contract(book, date, royalties)` → creates a contract

---

### Book

Represents a book.

#### Attributes:

 `title` (string)

#### Methods:

 `contracts()` → returns all contracts for the book
 `authors()` → returns unique authors of the book

---

### Contract

Represents the join model connecting Authors and Books.

#### Attributes:

* `author` (Author instance)
* `book` (Book instance)
* `date` (string)
* `royalties` (integer between 0–100)

---

## 🔗 Relationship Summary

| Model    | Relationship                       |
| -------- | ---------------------------------- |
| Author   | has many Books through Contracts   |
| Book     | has many Authors through Contracts |
| Contract | belongs to Author and Book         |

---

## Example Usage

```python
from lib.many_to_many import Author, Book, Contract

author1 = Author("Toni Morrison")
author2 = Author("Alice Walker")

book1 = Book("Collaborative Stories")

contract1 = Contract(author1, book1, "2026-03-29", 15)
contract2 = Contract(author2, book1, "2026-03-30", 12)

print(author1.books())   # [book1]
print(book1.authors())   # [author1, author2]
```

---

## Validation Rules

* Author name must be a non-empty string
* Book title must be a non-empty string
* Contract must:

  * link valid Author and Book instances
  * include a non-empty date string
  * have royalties between 0 and 100

---

## Learning Goals

By completing this lab, you will:

* Understand **many-to-many relationships**
* Use a **join class (Contract)** effectively
* Practice **data validation and encapsulation**
* Build scalable OOP models

---

## Author

Built as part of a Python OOP lab to master relationships and data modeling.

---
