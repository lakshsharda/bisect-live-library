"""Members and their loan limits."""
from dataclasses import dataclass

LOAN_LIMITS = {"standard": 3, "premium": 6}


@dataclass(frozen=True)
class Member:
    member_id: str
    name: str
    tier: str = "standard"


def loan_limit(member: Member) -> int:
    try:
        return LOAN_LIMITS[member.tier]
    except KeyError:
        raise ValueError(f"unknown tier: {member.tier!r}") from None
