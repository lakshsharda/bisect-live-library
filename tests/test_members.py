import pytest

from librarykit.members import Member, loan_limit


def test_loan_limits_by_tier():
    assert loan_limit(Member("m1", "Ana")) == 3
    assert loan_limit(Member("m2", "Ben", "premium")) == 6


def test_unknown_tier_is_rejected():
    with pytest.raises(ValueError):
        loan_limit(Member("m3", "Cy", "gold"))


def test_member_label():
    from librarykit.members import member_label

    assert member_label(Member("m1", "Ana")) == "Ana (standard)"


def test_is_premium():
    from librarykit.members import is_premium

    assert is_premium(Member("m2", "Ben", "premium")) and not is_premium(Member("m1", "Ana"))
