# librarykit

Small lending-library library: a catalog of books, members with loan limits, loans and late fines (integer cents, days as integers).

## Rules

- Standard members may hold 3 books, premium members 6.
- Loans last 14 days; the next 2 days are a free grace period.

## Usage

```python
from librarykit.catalog import Book, Catalog
from librarykit.loans import LoanDesk
```
