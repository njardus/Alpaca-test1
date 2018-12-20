from loguru import logger
import os
import time
import alpaca_trade_api as tradeapi
from universe import Universe

logger.info("Start algo script")

hardlimit = 10000

api = tradeapi.REST(
    key_id=os.environ['alpacakeyid'],
    secret_key=os.environ['alpacasecretkey'],
    base_url='https://paper-api.alpaca.markets'
)

def main():
    done = None
    logger.info("Start function")

    while True: #This runs indefinitely
        logger.debug("Start of the infinite while loop")

        # Get the server time, and see if the market is open
        clock = api.get_clock()
        now = clock.timestamp

        if clock.is_open and done != now.strftime('%Y-%m-%d'):
            logger.success("We're in the doing stuff place")
            done = now.strftime('%Y-%m-%d')
            logger.success(f'Done for {done}')
        else:
            logger.debug(f"clock.is_open = {clock.is_open}")
            logger.debug(f"now.strftime = {now.strftime('%Y-%m-%d')}")

        logger.debug('Iterate!')
        time.sleep(1)

    logger.info("Complete function")
