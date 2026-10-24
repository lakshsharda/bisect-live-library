"""The catalog of books: adding, looking up, searching."""
from dataclasses import dataclass


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    copies: int = 1


class Catalog:
    def __init__(self) -> None:
        self._books: dict[str, Book] = {}

    def __len__(self) -> int:
        return len(self._books)

    def add(self, book: Book) -> None:
        if book.isbn in self._books:
            raise ValueError(f"duplicate isbn: {book.isbn}")
        if book.copies < 1:
            raise ValueError("a book needs at least one copy")
        self._books[book.isbn] = book

    def get(self, isbn: str) -> Book:
        return self._books[isbn]

    def by_author(self, author: str) -> list[Book]:
        return sorted((b for b in self._books.values() if b.author == author), key=lambda b: b.title)

    def search(self, text: str) -> list[Book]:
        needle = text.lower()
        return sorted((b for b in self._books.values() if needle in b.title.lower()), key=lambda b: b.title)

    def titles_by_author(self, author: str) -> list[str]:
        return [b.title for b in self.by_author(author)]

    def copies_total(self) -> int:
        return sum(b.copies for b in self._books.values())
