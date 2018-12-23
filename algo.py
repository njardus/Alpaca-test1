from loguru import logger
import os
import time
from alpha_vantage.timeseries import TimeSeries

from universe import Universe
from universe import UniverseHoldings
import settings

logger.info("Start algo script")

hardlimit = 10000

ts = TimeSeries(key=os.environ['ALPHAVANTAGE_API_KEY'])

def main():
    done = None
    logger.info("Start function")

    while not done: #This runs indefinitely
        logger.debug("Start of the infinite while loop")
        data = None
        meta_data = None

        for index in UniverseHoldings:
            data, meta_data = ts.get_intraday(index)
            if (data != None) & (meta_data != None):
                logger.debug("data and meta_data are not empty anymore, so dump the data in a db")
                #TODO: Update dashboard using a new thread, and then turn into an indefinite loop again.
                # print(meta_data)
                # print(data)
                if index == UniverseHoldings[-1]:
                    time.sleep(settings.updatetime)
                    done = True
            else:
                logger.debug('Iterate!')
                time.sleep(1)

    logger.info("Complete function")
