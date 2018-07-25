"""Module from IQ Option API TBH pattern."""

from base import Base
import logging
import csv
import pickle
import talib
from talib import MA_Type
import pandas as pd
import numpy as np
import trendy

class TBH(Base):
    """Class for TBH pattern."""

    def __init__(self, api, active):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        super(TBH, self).__init__(api, active)
        self.name = "TBH"


    def call(self):
        """Method to check call pattern."""
        logger = logging.getLogger("__main__")
        candles = self.candles

        if hasattr(candles, 'candles_array'):
            candel_array = candles.candles_array
            close = pd.Series([candle.candle_close for candle in  candel_array])
            open = pd.Series([candle.candle_open for candle in  candel_array])
            high = pd.Series([candle.candle_high for candle in  candel_array])
            low = pd.Series([candle.candle_low for candle in  candel_array])
            up, lw, MA = talib.BBANDS(close, matype=MA_Type.T3)
            rsi14 = talib.RSI(close, timeperiod=14)
            ADX = talib.ADX(high, low, close, timeperiod=14)
            fastk, fastd = talib.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
            mac = talib.SMA(close , 10)
            men = np.asarray(abs(close - mac))
            float_data = [float(x) for x in men]
            lens = np.array(float_data)
            sma = talib.SMA(lens, 5)
            boom = np.asarray(sma)
            float_data1 = [float(y) for y in boom]
            boms = np.array(float_data1)
            MAX = max(open + close)
            MIN = min(open + close)
            logger.info("CandleType:'%s', lens:'%f', Boms:'%f'", candles.current_candle.candle_type, lens[-1], boms[-1])           
            if lens[-1] > (boms[-1]) and candles.current_candle.candle_type == "red": 
                return True

    def put(self):
        """Method to check put pattern."""
        logger = logging.getLogger("__main__")
        candles = self.candles

        if hasattr(candles, 'candles_array'):
            candel_array = candles.candles_array
            close = pd.Series([candle.candle_close for candle in  candel_array])
            open = pd.Series([candle.candle_open for candle in  candel_array])
            high = pd.Series([candle.candle_high for candle in  candel_array])
            low = pd.Series([candle.candle_low for candle in  candel_array])
            up, lw, MA = talib.BBANDS(close, matype=MA_Type.T3)
            rsi14 = talib.RSI(close, timeperiod=14)
            ADX = talib.ADX(high, low, close, timeperiod=14)
            fastk, fastd = talib.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
            mac = talib.SMA(close , 10)
            men = np.asarray(abs(close - mac))
            float_data = [float(x) for x in men]
            lens = np.array(float_data)
            sma = talib.SMA(lens, 5)
            boom = np.asarray(sma)
            float_data1 = [float(y) for y in boom]
            boms = np.array(float_data1)
            MAX = max(open + close)
            MIN = min(open + close)
            if lens[-1] > (boms[-1]) and candles.current_candle.candle_type == "green": 
                return True
