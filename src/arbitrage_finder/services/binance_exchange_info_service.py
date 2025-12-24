import httpx

from src.arbitrage_finder.models.price_store import PriceStore
from src.arbitrage_finder.services.binance_price_service import BinanceService


class BinanceExchangeInfoService(BinanceService):
    BASE_URL = "https://api.binance.com/api/v3/exchangeInfo"

    def __init__(self) -> None:

    async def get(self) -> PriceStore:
        price_store = PriceStore()
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(BinanceService.BASE_URL)
            response.raise_for_status()
            data = response.json()

            symbol = data["symbol"]
            price = float(data["price"])
            self._store.update(symbol, price)

        return self._store