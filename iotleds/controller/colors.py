from iotleds.bridge.message import SolidColor
from neopixel import NeoPixel
from math import pi, cos


def solid_color(msg: SolidColor, pixels: NeoPixel, **kwargs):
    pixels.fill(msg.color)
    pixels.show()


def get_rainbow_color(t: int, rgb_index: int) -> int:
    if DEAD_STARTS[rgb_index] <= t <= DEAD_ENDS[rgb_index]:
        return 0
    if rgb_index == 0 and t >= DEAD_ENDS[0]:
        return round(-1 * (AMP * cos(pi * (t + rgb_index * SPACING) / SPACING)) + AMP)
    return round(AMP * cos(pi * (t + rgb_index * SPACING) / SPACING) + AMP)


CYCLE = 750
SPACING = CYCLE/3
AMP = 100/2
DEAD_STARTS = [(i + 1) % 3 * SPACING for i in range(3)]
DEAD_ENDS = [ds + SPACING for ds in DEAD_STARTS]
RAINBOW_COLORS = [(get_rainbow_color(t, 0),
                   get_rainbow_color(t, 1),
                   get_rainbow_color(t, 2)) for t in range(750)]


def rainbow(msg, pixels: NeoPixel, **kwargs):
    free = kwargs['free']
    s = 0
    while free():
        for i in range(750):
            pixels[i] = RAINBOW_COLORS[(i+s) % 750]
        pixels.show()
        s += 1
        if s == 750:
            s = 0
