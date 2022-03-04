from dataclasses import dataclass
from datetime import datetime


@dataclass
class Department:
    number: int
    name: str
    date: datetime
