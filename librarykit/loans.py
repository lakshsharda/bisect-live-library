"""Checking books out and in."""
from dataclasses import dataclass

from .catalog import Catalog
from .fines import days_late, fine_cents
from .members import Member, loan_limit


class LoanError(Exception):
    pass


@dataclass
class Loan:
    member_id: str
    isbn: str
    borrowed_day: int


class LoanDesk:
    def __init__(self, catalog: Catalog) -> None:
        self.catalog = catalog
        self._loans: list[Loan] = []

    def loans_of(self, member: Member) -> list[Loan]:
        return [entry for entry in self._loans if entry.member_id == member.member_id]

    def copies_out(self, isbn: str) -> int:
        return sum(1 for loan in self._loans if loan.isbn == isbn)

    def checkout(self, member: Member, isbn: str, day: int) -> Loan:
        book = self.catalog.get(isbn)
        mine = self.loans_of(member)
        if any(loan.isbn == isbn for loan in mine):
            raise LoanError("already borrowed")
        if len(mine) >= loan_limit(member):
            raise LoanError("loan limit reached")
        if self.copies_out(isbn) >= book.copies:
            raise LoanError("no copy available")
        loan = Loan(member.member_id, isbn, day)
        self._loans.append(loan)
        return loan

    def return_book(self, member: Member, isbn: str, day: int) -> int:
        """Take a book back; returns the late fine in cents."""
        for loan in self._loans:
            if loan.member_id == member.member_id and loan.isbn == isbn:
                self._loans.remove(loan)
                return fine_cents(days_late(loan.borrowed_day, day))
        raise LoanError("not borrowed")

    def overdue_loans(self, day: int) -> list[Loan]:
        return [loan for loan in self._loans if days_late(loan.borrowed_day, day) > 0]
