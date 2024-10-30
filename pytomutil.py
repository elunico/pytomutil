class frange:
    def __init__(self, start: float, stop: float, step: float) -> None:
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return type(self)(self.start, self.stop, self.step)

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration()
        result = self.start
        self.start += self.step
        return result


def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b


class SRGBColor:
    def __init__(self, r: float, g: float, b: float, a: float = 1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def lerp(self, other: "SRGBColor", percent: float) -> "SRGBColor":
        return SRGBColor(
            lerp(self.r, other.r, percent),
            lerp(self.g, other.g, percent),
            lerp(self.b, other.b, percent),
            lerp(self.a, other.a, percent),
        )

    @property
    def luminance(self) -> float:
        """Given an sRGB color as 3 RGB values between 0 and 1, return their relative luminance"""
        return 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b

    def __str__(self) -> str:
        return "SRGBColor({}, {}, {}, {})".format(self.r, self.g, self.b, self.a)


if __name__ == "__main__":
    red = SRGBColor(1, 0, 0)
    green = SRGBColor(0, 1, 0)

    for i in frange(0, 1.01, 0.05):
        print(red.lerp(green, i), i)
