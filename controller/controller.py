from iotleds.bridge.client import MessageClient
from iotleds.bridge.message import Message, SolidColor
import board
import neopixel
from datetime import datetime
from threading import Thread, Lock
from .colors import solid_color


msg_functions = {
    SolidColor: solid_color
}


class LedController:

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 750, auto_write=False)
        self.lock = Lock()
        self.mc = MessageClient()
        self.mc.listen(self.message_handler)

    def message_handler(self, msg: Message):
        # Print a debug statement
        print("[{}] Received > {}".format(
            datetime.now().strftime("%I:%M%p"), msg)
        )

        led_process = Thread(target=self.run_leds, args=(msg,))
        led_process.start()

    def run_leds(self, msg: Message):
        """
        Dispatches a command to the LEDs in a thread-safe way.

        :param msg: The instruction for the LED Array
        :return: None
        """
        self.lock.acquire()
        # check if message is old?
        msg_functions[type(msg)](msg, self.pixels)
        self.lock.release()
