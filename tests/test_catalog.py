import pytest

from librarykit.catalog import Book, Catalog


def make():
    cat = Catalog()
    cat.add(Book("1", "Dune", "Herbert"))
    cat.add(Book("2", "Dune Messiah", "Herbert", copies=2))
    cat.add(Book("3", "Emma", "Austen"))
    return cat


def test_add_and_get():
    assert make().get("3").title == "Emma" and len(make()) == 3


def test_duplicate_isbn_is_rejected():
    with pytest.raises(ValueError, match="duplicate"):
        make().add(Book("1", "Other", "X"))


def test_a_book_needs_a_copy():
    with pytest.raises(ValueError):
        Catalog().add(Book("9", "Ghost", "X", copies=0))


def test_unknown_isbn():
    with pytest.raises(KeyError):
        make().get("404")


def test_by_author_is_sorted_by_title():
    assert [b.title for b in make().by_author("Herbert")] == ["Dune", "Dune Messiah"]


def test_search_ignores_case():
    assert [b.isbn for b in make().search("DUNE")] == ["1", "2"]


def test_search_with_no_match():
    assert make().search("zzz") == []


def test_titles_by_author():
    assert make().titles_by_author("Austen") == ["Emma"]


def test_copies_total():
    assert make().copies_total() == 4
