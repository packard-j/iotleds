from typing import TypeVar, Tuple


class SolidColor:

    def __init__(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self):
        return "SolidColor: {}".format(self.color)


Message = TypeVar('Message', SolidColor, str)

