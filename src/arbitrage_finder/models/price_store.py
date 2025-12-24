from typing import Dict
from datetime import datetime, timezone
from src.arbitrage_finder.models.price_snapshot import PriceSnapshot

class PriceStore:
    def __init__(self) -> None:
        self._prices: Dict[str, float] = {}

    def update(self, symbol: str, price: float) -> None:
        self._prices[symbol] = price

    def snapshot(self) -> PriceSnapshot:
        return PriceSnapshot(
            prices=self._prices.copy(),
            timestamp=datetime.now(timezone.utc)
        )