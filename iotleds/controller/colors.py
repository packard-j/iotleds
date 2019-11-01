from iotleds.bridge.message import Message, SolidColor, Cascade, Rainbow, Pattern
from neopixel import NeoPixel
from math import pi, cos
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
        self.colors = self.generate_2c(msg.colors[0], msg.colors[1], msg.n)

    def update(self, msg: Message):
        self.speed = msg.speed
        self.colors = self.generate_2c(msg.colors[0], msg.colors[1], msg.n)

    def run(self, **kwargs):
        free = kwargs['free']
        s = 0
        while free:
            for i in range(750):
                self.pixels[i] = self.colors[(i + s) % 750]
            self.pixels.show()
            s += self.speed
            if s == 750:
                s = 0

    @staticmethod
    def generate_2c(c1: Tuple[int, int, int], c2: Tuple[int, int, int], n: int):
        width_up = 750//(2*n)
        step = tuple(map(lambda a, b: (b - a)/width_up, c1, c2))
        pattern = [tuple(round(c1[i] + step[i]*n) for i in range(3)) for n in range(width_up)]
        pattern_copy = pattern.copy()
        pattern_copy.reverse()
        pattern.extend(pattern_copy)
        return [pattern[i % (2*width_up)] for i in range(750)]


class CascadeMode(Mode):

    def __init__(self, pixels: NeoPixel, msg: Cascade):
        super().__init__(pixels)
        self.color = msg.color
        self.pixels.fill((0, 0, 0))

    def update(self, msg: Cascade):
        self.color = msg.color

    def run(self, **kwargs):
        free = kwargs['free']
        while free():
            self.shift()

    def shift(self):
        for i in range(749, 0, -1):
            self.pixels[i] = self.pixels[i-1]
        self.pixels[0] = self.color
        self.pixels.show()


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
