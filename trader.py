"""Module for IQ Option API trader."""

import logging
import iqoptionapi.constants as api_constants
import time
import tamm


class Trader(object):
    """Calss for IQ Option API trader."""

    def __init__(self, api, active):
        self.api = api
        self.active = active
        self.martingale = tamm.Martingale()



    def start(self):
        """Method for start trader."""
        logger = logging.getLogger(__name__)

        logger.info("Trader for active '%s' started.", self.active)

        logger.info("Trader for active '%s' wait for signal.", self.active)

    def getResult(self):
        if self.api.is_successful:
            try:
                result = self.api.listinfodata.current_listinfodata.win
                return result
            except:
                return None
        else:
            print("result error")
            return None

    def last(self):
        print self.api.changebalance('real')

    def trade(self, signal):
        """Method for trade."""
        logger = logging.getLogger(__name__)
        result = self.getResult()
        self.martingale.calc(result)
        investAmount = self.martingale.getCurrentInvest()
        id_no = (self.api.buy(
                investAmount,
                api_constants.ACTIVES[self.active],
                signal.option,
                signal.direction))



        logger.info("Trader for active '%s' recived signal '%s'.", self.active, signal.direction)
        
        logger.info("Trader for active '%s' successfully buy in direction '%s'.",
                    self.active, signal.direction)
        print (self.api.buy.get_expiration_time(duration=1)-self.api.timesync.server_timestamp)





        
def create_trader(api, active):
    """Method for create trader.

    :param api: The IQ Option API.
    :param active: The trader active.
    """
    logger = logging.getLogger(__name__)
    logger.info("Create trader for active '%s'.", active)
    return Trader(api, active)
