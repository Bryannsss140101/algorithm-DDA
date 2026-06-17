from flask import Flask, render_template, request, jsonify
from algorithms.dda import DDA
from models.pixel import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/draw", methods=["POST"])
def draw():
    data = request.json
    p0 = Position(int(data['x0']), int(data['y0']))
    p1 = Position(int(data['x1']), int(data['y1']))
    color = RGB(data["r"], data["g"], data["b"])
    size = data["size"]

    points = DDA(p0, p1)

    pixels = []
    for point in points:
        pixel = Pixel(point, color, size)
        pixels.append(
            {
                "x": pixel.position.x,
                "y": pixel.position.y,
                "size": pixel.size,
                "color": pixel.color.to_hex(),
            }
        )

    return jsonify(pixels)


if __name__ == "__main__":
    app.run(debug=True)
