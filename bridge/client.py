from threading import Thread
from multiprocessing.connection import Client
from typing import Callable, Any
from .config import Config
from .message import Message


class MessageClient:

    def __init__(self):
        # Establish the connection to the message server
        try:
            self.connection = Client(Config.address)
        # Catch the exception caused by the message server not being up
        except ConnectionRefusedError:
            print("Error: Connection Refused. Did you remember to start the message server?")
            raise ConnectionRefusedError

    def listen(self, callback: Callable[[Message], Any]):
        """
        Listens for incoming messages from the MessageServer and executes the callback
        each time one is received.

        :param callback: The function to call with the received message
        :return: None
        """
        # Start the listener process
        listen_process = Thread(target=self._listen_worker, args=(callback,))
        listen_process.start()

    def _listen_worker(self, callback: Callable[[Message], Any]):
        """
        Internal listen function used in spawning the listen process.

        :param callback: The function to call with each received message
        :return: None
        """
        # Receive messages in a loop
        while True:
            # Execute the callback on each message
            try:
                msg = self.connection.recv()
                callback(msg)
            # Catch the error caused by the connection closing
            except EOFError:
                return
            # Allow the user to exit with Ctrl+C
            except KeyboardInterrupt:
                print("Exiting...")
                return
