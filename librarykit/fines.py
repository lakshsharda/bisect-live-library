"""Due days and late fines. Days are integers; money is integer cents."""
LOAN_DAYS = 14
GRACE_DAYS = 2
FINE_PER_DAY_CENTS = 25
FINE_CAP_CENTS = 1500


def due_day(borrowed_day: int) -> int:
    return borrowed_day + LOAN_DAYS


def days_late(borrowed_day: int, returned_day: int) -> int:
    """Whole days past the due day."""
    late = returned_day - due_day(borrowed_day)
    if late < 0:
        return 0
    return late


def fine_cents(late_days: int) -> int:
    billable = late_days - GRACE_DAYS
    if billable <= 0:
        return 0
    return min(billable * FINE_PER_DAY_CENTS, FINE_CAP_CENTS)
