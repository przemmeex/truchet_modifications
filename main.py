from typing import List, Tuple
from ttr_triangles_2 import *
from ttr_triangles_1 import *
from ttr_triangles_0 import *
import time
import random
from tkinter import *
from PIL import Image
import sys
import math

from ttruch_library import Triangle, FILL_B, SMALL_TTIANGLE_EDGE, WIDTH, HEIGHT, SPLIT_PROBABILITY_2_TO_1, SPLIT_PROBABILITY_1_TO_0


def generate_4_internal_triangles(triangle: Triangle) -> List[Triangle]:

    ys = [el[1] for el in triangle.get_coordinates()]
    xs = [el[0] for el in triangle.get_coordinates()]

    left_vertex_index = xs.index(min(xs))
    right_vertex_index = xs.index(max(xs))
    middle = [a for a in range(3)]
    middle.remove(left_vertex_index)
    middle.remove(right_vertex_index)
    middle_index = middle[0]

    triangle_edge = xs[right_vertex_index] - xs[left_vertex_index]

    t1 = Triangle([xs[middle_index], ys[middle_index]],
                  [xs[middle_index] - int(triangle_edge / 4), int(
                      ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)],
                  [xs[middle_index] + int(triangle_edge / 4), int(ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)])
    t2 = Triangle([xs[middle_index] - int(triangle_edge / 4), int(ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)],
                  [xs[left_vertex_index], ys[left_vertex_index]],
                  [xs[left_vertex_index] + int(triangle_edge / 2), ys[left_vertex_index]])
    t3 = Triangle([xs[middle_index], ys[left_vertex_index]],
                  [xs[middle_index] - int(triangle_edge / 4), int(
                      ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)],
                  [xs[middle_index] + int(triangle_edge / 4), int(ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)])
    t4 = Triangle([xs[middle_index] + int(triangle_edge / 4), int(ys[middle_index] - (ys[middle_index] - ys[left_vertex_index])/2)],
                  [xs[middle_index], ys[left_vertex_index]],
                  [xs[right_vertex_index], ys[right_vertex_index]])

    return [t1, t2, t3, t4]


def calculate_vertexes(board_width: int, board_height: int) -> Tuple[List[Triangle], List[Triangle], List[Triangle]]:

    triangle_edge = SMALL_TTIANGLE_EDGE*4
    trinagle_height = round(triangle_edge * math.sqrt(3)/2)
    triangles_1 = []
    triangles_2 = []
    i = 0
    row_offset = 0
    while i < board_height:
        up_triangles = generate_one_upwards_triangles_row(
            0-int(triangle_edge/2)+row_offset, trinagle_height+i, board_width+int(triangle_edge/2)+row_offset, triangle_edge)
        down_triangles = generate_one_downwards_triangles_row(
            0+row_offset, trinagle_height+i, board_width+row_offset, triangle_edge)
        triangles_2 += up_triangles
        triangles_2 += down_triangles
        i += trinagle_height
        if row_offset == 0:
            row_offset = -int(triangle_edge/2)
        else:
            row_offset = 0

    final_triangles_2 = []

    for i in triangles_2:
        if random.randrange(10) < SPLIT_PROBABILITY_2_TO_1:
            triangles_1 += generate_4_internal_triangles(i)
        else:
            final_triangles_2.append(i)

    final_triangles_0 = []
    final_triangles_1 = []

    for i in triangles_1:
        if random.randrange(10) < SPLIT_PROBABILITY_1_TO_0:
            final_triangles_0 += generate_4_internal_triangles(i)
        else:
            final_triangles_1.append(i)

    return final_triangles_0, final_triangles_1, final_triangles_2


def generate_one_upwards_triangles_row(start_x, start_y, end_x, triangle_edge) -> List[Triangle]:
    _triangles = []
    trinagle_height = round(triangle_edge * math.sqrt(3)/2)
    for x in range(start_x, end_x, triangle_edge):
        _triangles.append(Triangle(
            [x+int(triangle_edge/2), start_y-trinagle_height], [x, start_y], [x+triangle_edge, start_y]))
    return _triangles


def generate_one_downwards_triangles_row(start_x, start_y, end_x, triangle_edge):
    _triangles = []
    trinagle_height = round(triangle_edge * math.sqrt(3)/2)
    for x in range(start_x, end_x, triangle_edge):
        _triangles.append(Triangle([x+int(triangle_edge/2), start_y], [
                          x, start_y-trinagle_height], [x+triangle_edge, start_y-trinagle_height]))
    return _triangles


if __name__ == ("__main__"):
    master = Tk()

    canv = Canvas(master, width=WIDTH, height=HEIGHT)
    canv.create_rectangle(0, 0, WIDTH+5, HEIGHT+5, fill=FILL_B)
    canv.pack()
    triangles_0, triangles_1, triangles_2 = calculate_vertexes(WIDTH, HEIGHT)


    function_list = [draw_tringle_order_2_pattern_0,
                    draw_tringle_order_2_pattern_1]
    for i in triangles_2:
        triangle_2 = random.choice(function_list)
        triangle_2(i.get_coordinates(), canv)

    function_list = [draw_tringle_order_1_pattern_0,
                    draw_tringle_order_1_pattern_1]
    for i in triangles_1:
        triangle_1 = random.choice(function_list)
        triangle_1(i.get_coordinates(), canv)

    function_list = [draw_tringle_order_0_pattern_0,
                    draw_tringle_order_0_pattern_1,
                    draw_tringle_order_0_pattern_2]
    for i in triangles_0:
        triangle_0 = random.choice(function_list)
        triangle_0(i.get_coordinates(), canv)


    canv.update()
    canv.postscript(file="sq1.ps", colormode='color')
    # mainloop()
    img = Image.open("sq1.ps")
    sys.setrecursionlimit(img.size[1] ** 2)
    LIMIT = img.size[0]


    img.show()
    epoch_time = int(time.time())
    img.save("{0}.png".format(epoch_time))