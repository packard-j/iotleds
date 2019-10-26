from iotleds.bridge.message import SolidColor


def solid_color(pixels, msg: SolidColor):
    pixels.fill(msg.color)
