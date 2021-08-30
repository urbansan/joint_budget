from dataclasses import dataclass, field
import datetime


@dataclass(frozen=True)
class Transfer:
    transaction_data: datetime.date
    value: float
    currency: str
    title: str
    account_no_from: str
    account_no_to: str
    source_unique_id: str



