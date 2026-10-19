import pytest

from librarykit.members import Member, loan_limit


def test_loan_limits_by_tier():
    assert loan_limit(Member("m1", "Ana")) == 3
    assert loan_limit(Member("m2", "Ben", "premium")) == 6


def test_unknown_tier_is_rejected():
    with pytest.raises(ValueError):
        loan_limit(Member("m3", "Cy", "gold"))
