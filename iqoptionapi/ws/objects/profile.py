"""Module for IQ Option Profile websocket object."""

from iqoptionapi.ws.objects.base import Base


class Profile(Base):
    """Class for IQ Option Profile websocket object."""

    def __init__(self):
        super(Profile, self).__init__()
        self.__name = "profile"
        self.__skey = None
        self.__balance = None
        self.__balance_id = None

    @property
    def skey(self):
        """Property to get skey value.

        :returns: The skey value.
        """
        return self.__skey

    @skey.setter
    def skey(self, skey):
        """Method to set skey value."""
        self.__skey = skey

    @property
    def balance(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balance

    @balance.setter
    def balance(self, balance):
        """Method to set balance value."""
        self.__balance = balance

    @property
    def balance_id(self):
        """Property to get balance_id value.

        :returns: The balance value.
        """
        return self.__balance_id

    @balance_id.setter
    def balance_id(self, balance_id):
        """Method to set balance_id value."""
        self.__balance_id = balance_id
