import asyncio
import logging
from datetime import timedelta

from tinkoff.invest import CandleInterval
from tinkoff.invest.retrying.aio.client import AsyncRetryingClient
from tinkoff.invest.retrying.settings import RetryClientSettings
from tinkoff.invest.utils import now

from tinkoff.invest import (
    AsyncClient,
    CandleInstrument,
    InfoInstrument,
    SubscriptionInterval,
)
from tinkoff.invest.async_services import AsyncMarketDataStreamManager

from settings.comfig import Config

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)


async def main():
    config = Config()

    retry_settings = RetryClientSettings(use_retry=True, max_retry_attempt=2)

    async with AsyncRetryingClient(
        token=config.api_token.get_secret_value(),
        settings=retry_settings,
    ) as client:
    #     async for candle in client.get_all_candles(
    #         figi='BBG0047315Y7',
    #         from_=now() - timedelta(days=30),
    #         interval=CandleInterval.CANDLE_INTERVAL_HOUR,
    #     ):
    #         print(candle)
    #
    #     print(await client.users.get_accounts())

        market_data_stream: AsyncMarketDataStreamManager = (
            client.create_market_data_stream()
        )

        market_data_stream.candles.waiting_close().subscribe(
            [
                CandleInstrument(
                    figi='BBG0047315Y7',
                    interval=SubscriptionInterval.SUBSCRIPTION_INTERVAL_ONE_MINUTE
                )
            ]
        )

        async for marketdata in market_data_stream:
            print(marketdata)
            market_data_stream.info.subscribe([InfoInstrument(figi='BBG0047315Y7')])
            if marketdata.subscribe_info_response:
                print(marketdata.subscribe_info_response)
                market_data_stream.stop()


if __name__ == "__main__":
    asyncio.run(main())
