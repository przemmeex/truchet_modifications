from tkinter import *
from ttruch_library import SMALL_TTIANGLE_EDGE, calculate_start_angle, ARC_WIDTH, LINE_COLOUR
from typing import List, Tuple


Coordinates2D = Tuple[int]
VertexesCoordinates = List[Coordinates2D]


def draw_tringle_order_0_pattern_0(vertexes: VertexesCoordinates, surface_context: Canvas) -> None:
    # surface_context.create_line(
    #     vertexes[0][0], vertexes[0][1], vertexes[1][0], vertexes[1][1])
    # surface_context.create_line(
    #     vertexes[1][0], vertexes[1][1], vertexes[2][0], vertexes[2][1])
    # surface_context.create_line(
    #     vertexes[2][0], vertexes[2][1], vertexes[0][0], vertexes[0][1])

    start_angle = calculate_start_angle(vertexes)
    # top arc 0
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # top arc 1
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE * 3 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # top arc 2
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE * 5 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # "left" arc 0
    left_start_angle = 0
    if vertexes[1][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[1][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[1][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "right" arc 0
    left_start_angle = 0
    if vertexes[2][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[2][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[2][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "bottom" arc 0
    left_vertex_x = min(vertexes[1][0], vertexes[2][0])
    left_vertex_y = min(vertexes[1][1], vertexes[2][1])
    adjustment_angle = 180 if start_angle == 60 else 0
    surface_context.create_arc(
        round(left_vertex_x + SMALL_TTIANGLE_EDGE * 3 / 8),
        round(left_vertex_y - SMALL_TTIANGLE_EDGE * 1 / 8),
        round(left_vertex_x + SMALL_TTIANGLE_EDGE * 5 / 8),
        round(left_vertex_y + SMALL_TTIANGLE_EDGE * 1 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=adjustment_angle, extent=180)


def draw_tringle_order_0_pattern_1(vertexes: VertexesCoordinates, surface_context: Canvas) -> None:
    # surface_context.create_line(
    #     vertexes[0][0], vertexes[0][1], vertexes[1][0], vertexes[1][1])
    # surface_context.create_line(
    #     vertexes[1][0], vertexes[1][1], vertexes[2][0], vertexes[2][1])
    # surface_context.create_line(
    #     vertexes[2][0], vertexes[2][1], vertexes[0][0], vertexes[0][1])

    start_angle = calculate_start_angle(vertexes)
    # top arc 0
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # top arc 1
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE * 3 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # top arc 2
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE * 5 / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE * 5 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # "left" arc 0
    left_start_angle = 0
    if vertexes[1][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[1][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[1][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "right" arc 0
    left_start_angle = 0
    if vertexes[2][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[2][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[2][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "bottom" arc 0
    left_vertex_x = min(vertexes[1][0], vertexes[2][0])
    left_vertex_y = min(vertexes[1][1], vertexes[2][1])

    if start_angle == 60:
        surface_context.create_arc(
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_y - SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 3 / 8),
            round(left_vertex_y + SMALL_TTIANGLE_EDGE * 1 / 8),
            style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=300, extent=60)

        surface_context.create_arc(
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 5 / 8),
            round(left_vertex_y - SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 7 / 8),
            round(left_vertex_y + SMALL_TTIANGLE_EDGE * 1 / 8),
            style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=180, extent=60)

    elif start_angle == 240:
        surface_context.create_arc(
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_y - SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 3 / 8),
            round(left_vertex_y + SMALL_TTIANGLE_EDGE * 1 / 8),
            style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=0, extent=60)

        surface_context.create_arc(
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 5 / 8),
            round(left_vertex_y - SMALL_TTIANGLE_EDGE * 1 / 8),
            round(left_vertex_x + SMALL_TTIANGLE_EDGE * 7 / 8),
            round(left_vertex_y + SMALL_TTIANGLE_EDGE * 1 / 8),
            style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=120, extent=60)


def draw_tringle_order_0_pattern_2(vertexes: VertexesCoordinates, surface_context: Canvas) -> None:
    # surface_context.create_line(
    #     vertexes[0][0], vertexes[0][1], vertexes[1][0], vertexes[1][1])
    # surface_context.create_line(
    #     vertexes[1][0], vertexes[1][1], vertexes[2][0], vertexes[2][1])
    # surface_context.create_line(
    #     vertexes[2][0], vertexes[2][1], vertexes[0][0], vertexes[0][1])

    start_angle = calculate_start_angle(vertexes)
    # top arc 0
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # top arc 1
    surface_context.create_arc(
        round(vertexes[0][0]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][0]+SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[0][1]+SMALL_TTIANGLE_EDGE * 3 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=start_angle, extent=60)

    # "left" arc 0
    left_start_angle = 0
    if vertexes[1][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[1][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[1][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[1][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[1][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "left" arc 1
    surface_context.create_arc(
        round(vertexes[1][0]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[1][1]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[1][0]+SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[1][1]+SMALL_TTIANGLE_EDGE * 3 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)

    # "right" arc 0
    left_start_angle = 0
    if vertexes[2][0] < vertexes[0][0] and start_angle == 60:
        left_start_angle = 300
    elif vertexes[2][0] < vertexes[0][0] and start_angle == 240:
        left_start_angle = 0
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 60:
        left_start_angle = 180
    elif vertexes[2][0] > vertexes[0][0] and start_angle == 240:
        left_start_angle = 120

    surface_context.create_arc(
        round(vertexes[2][0]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]-SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][0]+SMALL_TTIANGLE_EDGE / 8),
        round(vertexes[2][1]+SMALL_TTIANGLE_EDGE / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)
    # "right" arc 1
    surface_context.create_arc(
        round(vertexes[2][0]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[2][1]-SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[2][0]+SMALL_TTIANGLE_EDGE * 3 / 8),
        round(vertexes[2][1]+SMALL_TTIANGLE_EDGE * 3 / 8),
        style="arc", width=ARC_WIDTH, outline=LINE_COLOUR, start=left_start_angle, extent=60)
