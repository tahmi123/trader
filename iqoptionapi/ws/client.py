"""Module for IQ option websocket."""

import json
import logging
import websocket


class WebsocketClient(object):
    """Class for work with IQ option websocket."""

    def __init__(self, api):
        """
        :param api: The instance of :class:`IQOptionAPI
            <iqoptionapi.api.IQOptionAPI>`.
        """
        self.api = api
        self.wss = websocket.WebSocketApp(
            self.api.wss_url, on_message=self.on_message,
            on_error=self.on_error, on_close=self.on_close,
            on_open=self.on_open)

    def on_message(self, wss, message): # pylint: disable=unused-argument
        """Method to process websocket messages."""
        logger = logging.getLogger(__name__)
        api_responce = message
        message = json.loads(str(message))

        if not (message["name"] == "timeSync" or
                message["name"] == "heartbeat" or
                message["name"] == "newChartData" or
                message["name"] == "tradersPulse"
               ):
            logger.debug(api_responce)

        if message["name"] == "timeSync":
            self.api.timesync.server_timestamp = message["msg"]
        if message["name"] == "profile":
            #--------------all-------------
            self.api.profile.msg=message["msg"]
            #---------------------------
            try:
                self.api.profile.balance = message["msg"]["balance"]
            except:
                pass
            
            try:
                self.api.profile.balance_id=message["msg"]["balance_id"]
            except:
                pass
            
            try:
                self.api.profile.balance_type=message["msg"]["balance_type"]
            except:
                pass

            try:
                self.api.profile.balances=message["msg"]["balances"]
            except:
                pass
            try:
                self.api.profile.skey = message["msg"]["skey"]
            except:
                pass

        if message["name"]=="api_game_betinfo_result":
            try:
                self.api.game_betinfo.isSuccessful=message["msg"]["isSuccessful"]
                self.api.game_betinfo.dict=message["msg"]["result"]["data"] 
            except:
                pass

        if message["name"] == "candles":
            self.api.candles.candles_data = message["msg"]["candles"]
            self.api.activeCandles[int(message["request_id"])] = self.api.candles
            # if message["request_id"] == "60":
            #     self.api.candles.candles_data = message["msg"]["data"]
            #     self.api.activeCandles[message["msg"]["active_id"]] = self.api.candles
            # if message["request_id"] == "300":
            #     self.api.candle5Mins.candles_data = message["msg"]["data"]
            #     self.api.active5MinCandles[message["msg"]["active_id"]] = self.api.candle5Mins

        if message["name"] == "buyComplete":
            self.api.buy_status = message["msg"]["isSuccessful"]
        
        if message["name"] == "listInfoData":
            listinfodata = lambda: None
            listinfodata.__dict__ = message["msg"][0]
            self.api.listinfodata.add_listinfodata(listinfodata)
            
    @staticmethod
    def on_error(wss, error): # pylint: disable=unused-argument
        """Method to process websocket errors."""
        print('in error')
        logger = logging.getLogger(__name__)
        logger.error(error)

    @staticmethod
    def on_open(wss): # pylint: disable=unused-argument
        """Method to process websocket open."""
        print('in open')
        logger = logging.getLogger(__name__)
        logger.debug("Websocket client connected.")

    @staticmethod
    def on_close(wss): # pylint: disable=unused-argument
        """Method to process websocket close."""
        print('on close')
        logger = logging.getLogger(__name__)
        logger.debug("Websocket connection closed.")
