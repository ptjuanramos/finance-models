import unittest
from typing import List

import unittest

from src.arbitrage_finder.models.price_store import PriceStore
from src.arbitrage_finder.services.binance_price_service import BinanceService


class BinanceServiceTest(unittest.IsolatedAsyncioTestCase):

    async def test_get(self) -> None:
        store = PriceStore()
        binance_service = BinanceService(pair, store)
        price_store = await binance_service.get()

        assert price_store is not None


if __name__ == '__main__':
    unittest.main()
