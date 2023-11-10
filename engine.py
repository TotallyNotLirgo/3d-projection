import pyray as pr
from calculations import transform_and_scale, get_rotation_matrix
import numpy as np
from constants import HEIGHT

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

rotation = [0, 0, 0]
camera_position = [0, 0, 0]

def render():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    rotation[0] += 0.01
    rotation[1] += 0.005
    rotation[2] += 0.003
    for edge in edges:
        vertex_1 = transform_and_scale(np.dot(get_rotation_matrix(*rotation), 
                                              np.subtract(vertices[edge[0]], camera_position)), HEIGHT / 1.5)
        vertex_2 = transform_and_scale(np.dot(get_rotation_matrix(*rotation), 
                                              np.subtract(vertices[edge[1]], camera_position)), HEIGHT / 1.5)
        pr.draw_line_v(vertex_1, vertex_2, pr.RED)
    pr.end_drawing()