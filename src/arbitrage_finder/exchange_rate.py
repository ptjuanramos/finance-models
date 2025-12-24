from dataclasses import dataclass

@dataclass(frozen=True)
class ExchangeRate:
    source: str
    target: str
    rate: float