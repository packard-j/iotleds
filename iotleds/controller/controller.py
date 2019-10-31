from iotleds.bridge.client import MessageClient
from iotleds.bridge.message import Message, SolidColor, Rainbow, Cascade
import board
import neopixel
from datetime import datetime
from queue import Queue, Full
from iotleds.controller.colors import SolidColorMode, CascadeMode, RainbowMode


class LedController:

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 750, auto_write=False)
        self.modes = {
            SolidColor: SolidColorMode,
            Cascade: CascadeMode,
            Rainbow: RainbowMode
        }
        self.mode = self.modes[SolidColor](self.pixels)
        self.message_queue = Queue(maxsize=10)
        self.mc = MessageClient()
        self.mc.listen(self.message_handler)

    def message_handler(self, msg: Message):
        # Print a debug statement
        print("[{}] Received > {}".format(
            datetime.now().strftime("%I:%M%p"), msg)
        )
        try:
            self.message_queue.put(msg, timeout=5.0)
        except Full:
            print("Ignored message {} — Timout occurred".format(msg))

    def start(self):
        while True:
            msg = self.message_queue.get()
            msg_mode = self.modes[type(msg)]
            if type(self.mode) == msg_mode:
                self.mode.update(msg)
            else:
                self.mode = msg_mode(self.pixels, msg)
                self.mode.run(free=lambda: self.message_queue.empty())


if __name__ == '__main__':
    controller = LedController()
    controller.start()

