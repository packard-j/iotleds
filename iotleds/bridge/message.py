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

    def __init__(self, color: Tuple[int, int, int], loop: bool):
        self.color = color
        self.loop = loop

    def __str__(self):
        return "Cascade: {}".format(self.color)


class Pattern:

    def __init__(self, colors: Tuple[Tuple[int, int, int], Tuple[int, int, int]],
                 n: int, speed: int):
        self.colors = colors
        self.n = n
        self.speed = speed

    def __str__(self):
        return "Pattern: {} to {} - {} iterations @ speed {}".format(
            self.colors[0], self.colors[1], self.n, self.speed
        )


Message = TypeVar('Message', SolidColor, Rainbow, Cascade, Pattern)

