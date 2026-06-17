from models.pixel import Position


def DDA(p0: Position, p1: Position) -> list:
    points = []

    dif_x = p1.x - p0.x
    dif_y = p1.y - p0.y

    steps = max(abs(dif_x), abs(dif_y))

    if steps == 0:
        points.append(Position(p0.x, p0.y))
        return points

    x_inc = dif_x / steps
    y_inc = dif_y / steps

    x = p0.x
    y = p0.y

    for _ in range(steps + 1):
        points.append(Position(round(x), round(y)))

        x += x_inc
        y += y_inc

    return points
