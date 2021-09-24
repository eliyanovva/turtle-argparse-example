"""
This module takes several command line arguments to construct a shape using the turtle library.
"""
from .shape import draw_shape
from.cli_arguments import DrawingParser

def draw():
    SIDES = 0
    ANGLE_DEGREES = 0
    LENGTH = 0
    PEN_COLOR = 'black'
    WAIT_TIME = 3

    parser = DrawingParser()
    parser.setup_arguments()
    args = parser.parse_args()
    
    SIDES = args.sides
    ANGLE_DEGREES = 180 - ((SIDES-2)*180)/SIDES

    if not args.length:
        LENGTH = 50 + args.big*50 + args.small*(-20)
    else:
        LENGTH = args.length
    
    if args.pen_color:
        PEN_COLOR = args.pen_color
    if args.time:
        WAIT_TIME = args.time

    draw_shape(ANGLE_DEGREES, SIDES, LENGTH, PEN_COLOR, WAIT_TIME)
