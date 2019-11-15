from iotleds.bridge.message import Message, SolidColor, Cascade, Rainbow, Pattern, Secret
from neopixel import NeoPixel
from math import pi, cos, sin
from typing import Tuple


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

    def run(self, **kwargs):
        self.pixels.fill(self.color)
        self.pixels.show()


class PatternMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Pattern):
        super().__init__(pixels)
        self.speed = msg.speed
        self.c1 = msg.colors[0]
        self.c2 = msg.colors[1]
        self.n = msg.n
        self.colors = self.generate_2c()
        self.offset = 0

    def update(self, msg: Message):
        self.speed = msg.speed
        # Any of the variables which affect the pattern
        if msg.n != self.n or msg.colors[0] != self.c1 or msg.colors[1] != self.c2:
            self.n = msg.n
            self.c1 = msg.colors[0]
            self.c2 = msg.colors[1]
            self.colors = self.generate_2c()

    def run(self, **kwargs):
        free = kwargs['free']
        while free():
            for i in range(750):
                self.pixels[i] = self.colors[(i + self.offset) % 750]
            self.pixels.show()
            self.offset = (self.offset + self.speed) % 750

    def generate_2c(self):
        width_up = 750 // (2 * self.n)
        step = tuple(map(lambda a, b: (b - a) / width_up, self.c1, self.c2))
        pattern = [tuple(round(self.c1[i] + step[i] * n) for i in range(3)) for n in range(width_up)]
        pattern_copy = pattern.copy()
        pattern_copy.reverse()
        pattern.extend(pattern_copy)
        return [pattern[i % (2 * width_up)] for i in range(750)]


class CascadeMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Cascade):
        super().__init__(pixels)
        if msg.color:
            self.color = msg.color
        else:
            self.color = (0, 0, 0)
        self.loop = msg.loop

    def update(self, msg: Cascade):
        if msg.color:
            self.color = msg.color
        if self.loop is not None:
            self.loop = msg.loop

    def run(self, **kwargs):
        free = kwargs['free']
        while free():
            self.shift()

    def shift(self):
        if self.loop:
            self.pixels[0] = self.pixels[749]
        else:
            self.pixels[0] = self.color
        for i in range(749, 0, -1):
            self.pixels[i] = self.pixels[i - 1]
        self.pixels.show()


CYCLE = 750
SPACING = CYCLE / 3
AMP = 100 / 2
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


class SecretMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Secret):
        super().__init__(pixels)
        self.color = (0, 0, 0)

    def run(self, **kwargs):

        free = kwargs['free']
        center = 128
        amplitude = 127
        frequency1 = 2.4  # or 1.666 for more variation
        frequency2 = 2.4  # or 2.666 for more variation
        frequency3 = 2.4  # or 3.666 for more variation
        # test if shift will actually change anything
        shift1 = 0
        shift2 = 2
        shift3 = 4

        while free():
            for i in range(50):  # completely guessing what number this should be
                if not free:
                    break

                red = round(sin(frequency1 * i + shift1) * amplitude + center)
                grn = round(sin(frequency2 * i + shift2) * amplitude + center)
                blu = round(sin(frequency3 * i + shift3) * amplitude + center)
                self.color = (red, grn, blu)
                self.pixels.fill(self.color)
                self.pixels.show()
                self.color = (0, 0, 0)
                self.pixels.fill(self.color)
                self.pixels.show()
