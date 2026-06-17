def clamp(valor: int) -> int:
    return max(0, min(valor, 255))


class RGB:
    def __init__(self, r: int, g: int, b: int):
        self.r = clamp(r)
        self.g = clamp(g)
        self.b = clamp(b)

    def to_hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


class Position:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Pixel:
    def __init__(
        self, position: Position, color: RGB = RGB(255, 255, 255), size: int = 1
    ):
        self.position = position
        self.color = color
        self.size = size
