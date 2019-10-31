from iotleds.bridge.message import Message, SolidColor, Cascade, Rainbow
from neopixel import NeoPixel
from math import pi, cos
from time import sleep


class Mode:

    def __init__(self, pixels: NeoPixel):
        self.pixels = pixels

    def update(self, msg: Message):
        pass

    def run(self, **kwargs):
        pass


class SolidColorMode(Mode):

    def __init__(self, pixels: NeoPixel, msg=SolidColor((0, 0, 0))):
        super().__init__(pixels)
        self.color = msg.color

    def update(self, msg: SolidColor):
        self.color = msg.color
        self.run()

    def run(self, **kwargs):
        self.pixels.fill(self.color)
        self.pixels.show()


class CascadeMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Cascade):
        super().__init__(pixels)
        self.color = msg.color
        self.pixel_colors = [(0, 0, 0)] * 750

    def update(self, msg: Cascade):
        self.color = msg.color
        sleep(0.1)

    def run(self, **kwargs):
        free = kwargs['free']
        while free():
            self.shift(self.pixels)
            sleep(0.1)

    def shift(self, pixels: NeoPixel):
        for i in range(749):
            self.pixel_colors[i+1] = self.pixel_colors[i]
        self.pixel_colors[0] = self.color
        for i in range(750):
            self.pixels[i] = self.pixel_colors[i]
        self.pixels.show()
        print(self.pixel_colors[0:20])


CYCLE = 750
SPACING = CYCLE/3
AMP = 100/2
DEAD_STARTS = [(i + 1) % 3 * SPACING for i in range(3)]
DEAD_ENDS = [ds + SPACING for ds in DEAD_STARTS]


class RainbowMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Rainbow):
        super().__init__(pixels)
        self.rainbow_colors = [
            (self.get_rainbow_color(t, 0),
             self.get_rainbow_color(t, 1),
             self.get_rainbow_color(t, 2)) for t in range(750)]

    @staticmethod
    def get_rainbow_color(t: int, rgb_index: int) -> int:
        if DEAD_STARTS[rgb_index] <= t <= DEAD_ENDS[rgb_index]:
            return 0
        if rgb_index == 0 and t >= DEAD_ENDS[0]:
            return round(-1 * (AMP * cos(pi * (t + rgb_index * SPACING) / SPACING)) + AMP)
        return round(AMP * cos(pi * (t + rgb_index * SPACING) / SPACING) + AMP)

    def run(self, **kwargs):
        free = kwargs['free']
        s = 0
        while free():
            for i in range(750):
                self.pixels[i] = self.rainbow_colors[(i + s) % 750]
            self.pixels.show()
            s += 2
            if s == 750:
                s = 0
