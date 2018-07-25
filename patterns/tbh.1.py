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
            sigs = trendy.iterlines(close,open,high,low, window = 1/3.0 , charts = False)
            
            # K, D = self.stoc_occilator(candles=candles)
            aroon_up, aroon_down = talib.AROON(high, low, timeperiod=3)

            # loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
            # predicted_price = loaded_model.predict([[up[26] - candles.first_candle.candle_close, lw[26] - candles.first_candle.candle_close, candles.first_candle.candle_height - candles.second_candle.candle_height, rsi14[28], K[28], D[28], aroon_up[29], aroon_down[29]]])
            #logger.info("CandleClose:'%d', CandleOpen:'%d', CandleType:'%s', BBUp:'%d', BBLow:'%d', RSI: '%d', ARUp:'%d', ARDown:'%d', buy:'%d'", candles.current_candle.candle_close,candles.current_candle.candle_open,candles.current_candle.candle_type, up[27], lw[27], rsi14[27], aroon_up[27], aroon_down[27],sigs[27])

            if candles.current_candle.candle_close < candles.current_candle.candle_open:#candles.current_candle.candle_close > MA[27] and candles.current_candle.candle_open < MA[27] and aroon_up[27]==0 and aroon_up[27]==0:

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
            sigs = trendy.iterlines(close,open,high,low, window = 1/3.0 , charts = False)
            
            # K, D = self.stoc_occilator(candles=candles)
            aroon_up, aroon_down = talib.AROON(high, low, timeperiod=3)

            # loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
            # predicted_price = loaded_model.predict([[up[26] - candles.first_candle.candle_close, lw[26] - candles.first_candle.candle_close, candles.first_candle.candle_height - candles.second_candle.candle_height, rsi14[28], K[28], D[28], aroon_up[29], aroon_down[29]]])

            if candles.current_candle.candle_close > candles.current_candle.candle_open :#candles.current_candle.candle_close > MA[27] and candles.current_candle.candle_open < MA[27] and aroon_up[27]==0 and aroon_up[27]==0:

                return True
