from loguru import logger
# import btest
import algo
# import alpaca_trade_api as tradeapi

# Todo: Implement backtesting
# Todo: Implement paper trading

logger.info("Project name: Alpha-Vantage-test1")
logger.info("--------------------------")
logger.info("Program started")

if __name__ == '__main__':
    logger.info("__name__ is __main__, so enter main program.")
    algo.main()