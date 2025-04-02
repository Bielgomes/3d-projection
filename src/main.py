from math import cos, sin

import numpy as np
from pygame import QUIT, Clock, display, draw, event, init, quit

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
FPS = 60
is_running = True
angle = 0

X_OFFSET = WIDTH // 2
Y_OFFSET = HEIGHT // 2
SCALE = 100
PROJECTION_MATRIX = np.matrix([[1, 0, 0], [0, 1, 0]])

init()

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Simple Pygame 3D Projection")

points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))

points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projected_points = [[0, 0] for _ in range(len(points))]


def connect_points(point1: int, point2: int, projected_points: list):
    draw.line(
        screen,
        RED,
        projected_points[point1],
        projected_points[point2],
        1,
    )


clock = Clock()
while is_running:
    # set the frame rate
    clock.tick(FPS)
    # clear the screen
    screen.fill(WHITE)

    # handle GUI events
    for e in event.get():
        if e.type == QUIT:
            is_running = False

    rotation_matrix_x = np.matrix(
        [[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]]
    )
    rotation_matrix_y = np.matrix(
        [[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]]
    )
    rotation_matrix_z = np.matrix(
        [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
    )
    angle += 0.01

    # Draw the points
    for index, point in enumerate(points):
        rotated_point = (
            rotation_matrix_x
            * rotation_matrix_y
            * rotation_matrix_z
            * point.reshape(3, 1)
        )
        projected_point = PROJECTION_MATRIX * rotated_point

        x = int(projected_point[0, 0] * SCALE) + X_OFFSET
        y = int(projected_point[1, 0] * SCALE) + Y_OFFSET

        # update the projected points list
        projected_points[index] = (x, y)

        draw.circle(screen, RED, (x, y), 5)

    for point_index in range(4):
        connect_points(point_index, (point_index + 1) % 4, projected_points)
        connect_points(point_index + 4, ((point_index + 1) % 4) + 4, projected_points)
        connect_points(point_index, (point_index + 4), projected_points)

    # update the full display Surface to the screen
    display.flip()


quit()
