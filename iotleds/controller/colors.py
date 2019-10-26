from iotleds.bridge.message import SolidColor


def solid_color(msg: SolidColor, pixels):
    pixels.fill(msg.color)
    pixels.show()

