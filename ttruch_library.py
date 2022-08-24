from tkinter import *
import math
from typing import List, Tuple

# FILL_B = '#ffffff'
# FILL_B = '#223322'
FILL_B = '#357A4E'
LINE_COLOUR = '#B7FBD0'
ARC_WIDTH = 3
SMALL_TTIANGLE_EDGE = 60
SIZES_OF_TRIANGLES = 4
WIDTH, HEIGHT = 1000, 1000
SPLIT_PROBABILITY_2_TO_1 = 7
SPLIT_PROBABILITY_1_TO_0 = 5


Vector = List[List[int]]
Coordinates2D = Tuple[int]
VertexesCoordinates = List[Coordinates2D]


class EuclidMathHelper:
    @staticmethod
    def line_equation(x1, y1, x2, y2):
        a = math.inf if x1 == x2 else (y1-y2)/(x1-x2)
        b = 0 if x1 == x2 else y1 - x1 * a
        return a, b

    @staticmethod
    def angle_between_lines(a1, a2):
        return math.degrees(math.atan(abs((a1-a2)/(1+a1*a2))))

    @staticmethod
    def calculate_triangle_mass_cenre_coordinates(vertexes: VertexesCoordinates) -> Coordinates2D:
        x_final = sum(row[0] for row in vertexes)/3
        y_final = sum(row[1] for row in vertexes)/3
        return x_final, y_final


class Triangle:
    """_summary_
    """

    def __init__(self, a, b, c):
        self.vertex_a = a
        self.vertex_b = b
        self.vertex_c = c

    def get_coordinates(self) -> VertexesCoordinates:
        return (self.vertex_a, self.vertex_b, self.vertex_c)


def calculate_start_angle(vertexes: VertexesCoordinates) -> int:
    x_center, y_center = EuclidMathHelper.calculate_triangle_mass_cenre_coordinates(
        vertexes)
    A, B = EuclidMathHelper.line_equation(
        vertexes[0][0], vertexes[0][1], x_center, y_center)

    direction_angle = round(math.degrees(math.atan(A)))
    if direction_angle == 90 and vertexes[0][1] > y_center:
        direction_angle = -90
    elif direction_angle == 90:
        direction_angle = 0
    elif vertexes[0][1] > y_center:
        direction_angle -= 90

    angle = 240 + 2 * direction_angle

    return angle


def arc_converter(point_a_x, point_a_y, point_b_x, point_b_y, invert=True) -> Tuple[int, int, int, int, int]:
    d = math.sqrt((point_b_y-point_a_y)**2+(point_a_x-point_b_x)**2)
    middle_x = abs(point_a_x-point_b_x)/2 + min(point_a_x, point_b_x)
    middle_y = abs(point_a_y-point_b_y)/2 + min(point_a_y, point_b_y)

    alpha_angle = math.degrees(
        math.atan(abs((point_b_y-point_a_y)/(point_b_x-point_a_x))))
    if invert:
        alpha_angle += 180
    if (point_b_x > point_a_x and point_b_y > point_a_y) or (point_b_x < point_a_x and point_b_y < point_a_y):
        alpha_angle = 360-alpha_angle

    return middle_x-d/2, middle_y-d/2, middle_x+d/2, middle_y+d/2, alpha_angle
