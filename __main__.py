from general.config import get_config
from general.logger import init_logger
from logging import getLogger
import pyray as pr
import numpy as np
import math

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)

WIDTH = 800
HEIGHT = 450
DISTANCE = 4

vertices = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1,  1],
    [-1,  1, -1],
    [ 1,  1, -1],
    [ 1,  1,  1],
    [ 1, -1,  1],
    [ 1, -1, -1],
]
edges = [
    [0, 1], [1, 2], [2, 3], [3, 4],
    [4, 5], [5, 6], [6, 7], [7, 0],
    [0, 3], [1, 6], [2, 5], [4, 7]
]

def transform_and_scale(vertex, scale):
    v = [0, 0]
    v[0] = vertex[0] * scale / (DISTANCE - vertex[2]) + WIDTH  / 2 
    v[1] = vertex[1] * scale / (DISTANCE - vertex[2]) + HEIGHT / 2 
    return v

def get_rotation_matrix(x, y, z):
    M = [
        [
            [           1,            0,            0],
            [           0,  math.cos(x),  math.sin(x)],
            [           0, -math.sin(x),  math.cos(x)]
        ],
        [
            [ math.cos(y),            0, -math.sin(y)],
            [           0,            1,            0],
            [ math.sin(y),            0,  math.cos(y)]
        ],
        [
            [ math.cos(z),  math.sin(z),            0],
            [-math.sin(z),  math.cos(z),            0],
            [           0,            0,            1]
        ]
    ]
    return np.dot(np.dot(M[0], M[1]), M[2])

def main():
    pr.init_window(WIDTH, HEIGHT, "Hello Pyray")
    pr.set_target_fps(60)
    rotation = [0, 0, 0]
    camera_position = [0, 0, 0]

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        rotation[0] += 0.01
        rotation[1] += 0.005
        rotation[2] += 0.003
        for edge in edges:
            
            vertex_1 = transform_and_scale(np.dot(get_rotation_matrix(*rotation), np.subtract(vertices[edge[0]], camera_position)), HEIGHT / 1.5)
            vertex_2 = transform_and_scale(np.dot(get_rotation_matrix(*rotation), np.subtract(vertices[edge[1]], camera_position)), HEIGHT / 1.5)
            pr.draw_line_v(vertex_1, vertex_2, pr.RED)
        pr.end_drawing()
    pr.close_window()


if __name__ == "__main__":
    main()