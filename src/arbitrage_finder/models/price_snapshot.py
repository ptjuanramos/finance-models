from dataclasses import dataclass
from sqlite3 import Timestamp
from typing import Dict

@dataclass(frozen=True)
class PriceSnapshot:
    prices: Dict[str, float]
    timestamp: Timestamp