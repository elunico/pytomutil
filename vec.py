import random
import math

from pytomutil import lerp


class Vec2D:
    """
    Represents a 2-dimensional vector. An (x, y) pair
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_magnitude_and_angle(cls, magnitude: float, angle: float) -> "Vec2D":
        x = magnitude * math.cos(angle)
        y = magnitude * math.sin(angle)
        return cls(x, y)

    @property
    def polar(self) -> tuple[float, float]:
        return (self.magnitude, self.heading)

    @classmethod
    def zero(cls) -> "Vec2D":
        return cls(0, 0)

    @classmethod
    def random(cls, *, mag: float = 1.0) -> "Vec2D":
        angle = random.random() * math.pi * 2
        return cls.from_magnitude_and_angle(mag, angle)

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @magnitude.setter
    def magnitude(self, value: float):
        self.normalize()
        self *= value

    @property
    def magSquared(self) -> float:
        return self.magnitude**2

    def limit(self, maximum: float):
        m = self.magnitude
        if m > maximum:
            self.magnitude = maximum

    def limited(self, maximum: float) -> "Vec2D":
        result = self.copy()
        result.limit(maximum)
        return result

    def rotate(self, angle: float):
        self.heading = self.heading + angle

    def rotated(self, angle: float) -> "Vec2D":
        result = self.copy()
        result.rotate(angle)
        return result

    def lerp(self, other: "Vec2D", percent: float) -> None:
        self.x = lerp(self.x, other.x, percent)
        self.y = lerp(self.y, other.y, percent)

    def lerped(self, other: "Vec2D", percent: float) -> "Vec2D":
        result = self.copy()
        result.lerp(other, percent)
        return result

    def distance_to(self, other: "Vec2D") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot(self, other: "Vec2D") -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: "Vec2D") -> float:
        return math.acos(self.dot(other) / (self.magnitude * other.magnitude))

    @property
    def heading(self) -> float:
        return math.atan2(self.y, self.x)

    @heading.setter
    def heading(self, angle: float) -> None:
        m = self.magnitude
        self.x = math.cos(angle) * m
        self.y = math.sin(angle) * m

    def normalize(self) -> None:
        mag = self.magnitude
        self.x /= mag
        self.y /= mag

    def normalized(self) -> "Vec2D":
        result = self.copy()
        result.normalize()
        return result

    def copy(self):
        return Vec2D(self.x, self.y)

    def __complex__(self) -> complex:
        return self.x + self.y * 1j

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Vec2D):
            return NotImplemented

        return value.x == self.x and value.y == self.y

    def __hash__(self) -> int:
        code = hash(self.x)
        code ^= hash(self.y)
        return code

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vec2D(x={self.x}, y={self.y})"

    def __neg__(self) -> "Vec2D":
        return Vec2D(-self.x, -self.y)

    def __add__(self, other: "Vec2D") -> "Vec2D":
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2D") -> "Vec2D":
        if not isinstance(other, Vec2D):
            return NotImplemented
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int) -> "Vec2D":
        if not isinstance(other, (float, int)):
            return NotImplemented
        return Vec2D(self.x * other, self.y * other)

    def __truediv__(self, other: float | int) -> "Vec2D":
        if not isinstance(other, (float, int)):
            return NotImplemented
        return Vec2D(self.x / other, self.y / other)

    def __floordiv__(self, other: float | int) -> "Vec2D":
        if not isinstance(other, (float, int)):
            return NotImplemented
        return Vec2D(self.x // other, self.y // other)

    def __iadd__(self, other: "Vec2D") -> None:
        if not isinstance(other, Vec2D):
            return NotImplemented
        self.x += other.x
        self.y += other.y

    def __isub__(self, other: "Vec2D") -> None:
        if not isinstance(other, Vec2D):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, other: float | int) -> None:
        if not isinstance(other, (float, int)):
            return NotImplemented
        self.x *= other
        self.y *= other

    def __itruediv__(self, other: float | int) -> None:
        if not isinstance(other, (float, int)):
            return NotImplemented
        self.x /= other
        self.y /= other

    def __ifloordiv__(self, other: float | int) -> None:
        if not isinstance(other, (float, int)):
            return NotImplemented
        self.x //= other
        self.y //= other
