from math import sin, cos
from constants import DISTANCE, WIDTH, HEIGHT
import numpy as np

def transform_and_scale(vertex, scale):
    v = [0, 0]
    v[0] = vertex[0] * scale / (DISTANCE - vertex[2]) + WIDTH  / 2 
    v[1] = vertex[1] * scale / (DISTANCE - vertex[2]) + HEIGHT / 2 
    return v

def get_rotation_matrix(x, y, z):
    M = [
        [
            [      1,       0,       0],
            [      0,  cos(x),  sin(x)],
            [      0, -sin(x),  cos(x)]
        ],
        [
            [ cos(y),       0, -sin(y)],
            [      0,       1,       0],
            [ sin(y),       0,  cos(y)]
        ],
        [
            [ cos(z),  sin(z),       0],
            [-sin(z),  cos(z),       0],
            [      0,       0,       1]
        ]
    ]
    return np.dot(np.dot(M[0], M[1]), M[2])
