import pytest

from librarykit.catalog import Book, Catalog
from librarykit.loans import LoanDesk, LoanError
from librarykit.members import Member


@pytest.fixture
def desk():
    cat = Catalog()
    for i in range(8):
        cat.add(Book(str(i), f"Book {i}", "Author"))
    cat.add(Book("rare", "Rare", "Author", copies=1))
    return LoanDesk(cat)


ANA = Member("m1", "Ana")
BEN = Member("m2", "Ben", "premium")


def test_checkout_records_a_loan(desk):
    loan = desk.checkout(ANA, "0", 5)
    assert loan.borrowed_day == 5 and desk.loans_of(ANA) == [loan]


def test_standard_members_may_borrow_three(desk):
    for i in range(3):
        desk.checkout(ANA, str(i), 1)
    with pytest.raises(LoanError, match="limit"):
        desk.checkout(ANA, "3", 1)


def test_premium_members_may_borrow_six(desk):
    for i in range(6):
        desk.checkout(BEN, str(i), 1)
    with pytest.raises(LoanError, match="limit"):
        desk.checkout(BEN, "6", 1)


def test_the_same_book_cannot_be_borrowed_twice(desk):
    desk.checkout(ANA, "0", 1)
    with pytest.raises(LoanError, match="already"):
        desk.checkout(ANA, "0", 2)


def test_a_single_copy_goes_to_one_member_at_a_time(desk):
    desk.checkout(ANA, "rare", 1)
    with pytest.raises(LoanError, match="no copy"):
        desk.checkout(BEN, "rare", 1)
