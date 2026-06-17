import tkinter as tk

from algorithms.dda import DDA
from graphics.screen import Screen

from models.pixel import *


class App:
    def __init__(
        self,
        name: str = "Algorithm Digital Differential Analyzer",
        width: int = 800,
        height: int = 600,
    ):
        self.root = tk.Tk()
        self.root.title(name)

        # Panel lateral
        self.controls = tk.Frame(self.root)
        self.controls.pack(side="left", fill="y", padx=10)

        # Canvas
        self.canvas = tk.Canvas(
            self.root, width=width, height=height, bg="black", highlightthickness=0
        )
        self.canvas.pack(side="right")

        self.screen = Screen(self.canvas)

        self.p0 = None
        self.p1 = None

        # Sliders RGB
        self.r_scale = tk.Scale(
            self.controls,
            from_=0,
            to=255,
            orient="horizontal",
            label="Red",
            command=self.update_color_preview,
        )
        self.r_scale.set(255)
        self.r_scale.pack()

        self.g_scale = tk.Scale(
            self.controls,
            from_=0,
            to=255,
            orient="horizontal",
            label="Green",
            command=self.update_color_preview,
        )
        self.g_scale.set(255)
        self.g_scale.pack()

        self.b_scale = tk.Scale(
            self.controls,
            from_=0,
            to=255,
            orient="horizontal",
            label="Blue",
            command=self.update_color_preview,
        )
        self.b_scale.set(255)
        self.b_scale.pack()

        # Vista previa del color
        self.preview = tk.Label(
            self.controls,
            width=10,
            height=2,
            bg="#ffffff",
            relief="solid",
        )
        self.preview.pack(pady=10)

        # Tamaño del pixel
        self.size_scale = tk.Scale(
            self.controls, from_=1, to=20, orient="horizontal", label="Pixel Size"
        )
        self.size_scale.set(2)
        self.size_scale.pack()

        # Boton Clear
        self.clear_button = tk.Button(
            self.controls,
            text="Clear",
            command=self.clear_canvas,
        )
        self.clear_button.pack(pady=10)

        # Eventos
        self.canvas.bind("<Button-1>", self.on_click)

        # Atajo teclado
        self.root.bind("c", lambda e: self.clear_canvas())

    def update_color_preview(self, _=None):
        color = RGB(
            self.r_scale.get(),
            self.g_scale.get(),
            self.b_scale.get(),
        )

        self.preview.config(bg=color.to_hex())

    def update_size_label(self, value):
        self.size_label.config(text=f"Size: {value}")

    def clear_canvas(self):
        self.canvas.delete("all")

        self.p0 = None
        self.p1 = None

    def draw_points(self, points):
        color = RGB(
            self.r_scale.get(),
            self.g_scale.get(),
            self.b_scale.get(),
        )

        size = self.size_scale.get()

        for point in points:
            self.screen.put_pixel(Pixel(point, color, size))

    def on_click(self, event):

        if self.p0 is None:
            self.p0 = Position(event.x, event.y)

        elif self.p1 is None:
            self.p1 = Position(event.x, event.y)

            points = DDA(self.p0, self.p1)

            self.draw_points(points)

            self.p0 = None
            self.p1 = None

    def run(self):
        self.root.mainloop()
