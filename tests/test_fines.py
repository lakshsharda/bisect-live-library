from librarykit.fines import days_late, due_day, fine_cents


def test_due_day_is_two_weeks_later():
    assert due_day(10) == 24


def test_returning_early_or_on_the_due_day_is_not_late():
    assert days_late(0, 5) == 0
    assert days_late(0, 14) == 0


def test_days_late_counts_whole_days():
    assert days_late(0, 17) == 3


def test_no_fine_when_not_late():
    assert fine_cents(0) == 0


def test_grace_days_are_free():
    assert fine_cents(2) == 0


def test_first_day_after_grace_costs_one_day():
    assert fine_cents(3) == 25


def test_fine_grows_per_day():
    assert fine_cents(10) == 200


def test_fine_is_capped():
    assert fine_cents(100) == 1500
