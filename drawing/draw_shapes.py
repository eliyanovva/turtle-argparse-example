"""
This module takes several command line arguments to construct a shape using the turtle library.
"""
from .shape import draw_shape
from.cli_arguments import DrawingParser

def draw():
    sides = 0
    angle_degrees = 0
    length = 0
    pen_color = 'black'
    wait_time = 3

    parser = DrawingParser()
    parser.setup_arguments()
    args = parser.parse_args()

    sides = args.sides
    angle_degrees = 180 - ((sides-2)*180)/sides

    if not args.length:
        length = 50 + args.big*50 + args.small*(-20)
    else:
        length = args.length

    if args.pen_color:
        pen_color = args.pen_color
    if args.time:
        wait_time = args.time

    draw_shape(angle_degrees, sides, length, pen_color, wait_time)
