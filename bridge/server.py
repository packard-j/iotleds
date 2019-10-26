from multiprocessing.connection import Listener
from .config import Config
from .message import Message


class MessageServer:

    def __init__(self):
        self.listener = Listener(Config.address)
        self.connection = None

    def connect(self):
        """
        Connect to the message client.
        """
        self.connection = self.listener.accept()

    def send(self, message: Message):
        """
        Send a message to the client.

        :param message: The message to send
        :return: None
        """
        self.connection.send(message)

    def close(self):
        """
        Close the connection to the client.
        """
        self.connection.close()
