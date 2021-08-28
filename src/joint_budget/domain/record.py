from dataclasses import dataclass, field
import datetime


@dataclass(frozen=True)
class Record:
    transaction_data: datetime.date
    value: float
    currency: str
    title: str
    account_no: str
    source_unique_id: str



