from models.pixel import Pixel


class Screen:
    def __init__(self, canvas):
        self.canvas = canvas

    def put_pixel(self, pixel: Pixel):
        self.canvas.create_rectangle(
            pixel.position.x,
            pixel.position.y,
            pixel.position.x + pixel.size,
            pixel.position.y + pixel.size,
            fill=pixel.color.to_hex(),
            outline="",
        )
