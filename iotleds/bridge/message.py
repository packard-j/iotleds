from typing import TypeVar, Tuple


class SolidColor:

    def __init__(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self):
        return "SolidColor: {}".format(self.color)


class Rainbow:

    def __str__(self):
        return "Rainbow"


class Cascade:

    def __init__(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self):
        return "Cascade: {}".format(self.color)


class Pattern:

    def __init__(self):
        pass

    def __str__(self):
        return "Pattern"


Message = TypeVar('Message', SolidColor, Rainbow, Cascade, Pattern)

