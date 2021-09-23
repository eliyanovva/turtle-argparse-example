"""
This module takes several command line arguments to construct a shape using the turtle library.
"""
import argparse

from shape import draw_shape

SIDES = 0
ANGLE_DEGREES = 0
LENGTH = 0
PEN_COLOR = 'black'
WAIT_TIME = 3

# The ArgumentParser class is initialized.
parser = argparse.ArgumentParser(
    description='Use this module to print your own shape!',
    epilog='Thanks for stopping by!'
    )

# Optional arguments starting with '--' are added.
# action = 'store_true' enables them to be called without giving them a value.
parser.add_argument(
    '--big', help = 'Makes the side of the shape 100 pixels.'#, action = 'store_true'    
)
parser.add_argument(
    '--small', help = 'Makes the side of the shape 30 pixels.', action = 'store_true'
)
parser.add_argument(
    '--length', help = 'Sets the length of the side of a shape to a custom value.', type = int
)
# Some more optional arguments, which will require a value:
parser.add_argument(
    '--pen-color', help = 'Sets the color of the pen to a given color.'
)
# The default type of the arguments is string, 
# which is why this argument is specifically set to be an int.
parser.add_argument(
    '--time',
    help = 'Sets the time to wait after the shape is completed in seconds, defaults to 3 seconds.',
    type = int
)
# Finally, this is a required argument.
parser.add_argument(
    'sides',
    help = 'Specifies the selected shape, which can be a SQUARE, a TRIANGLE, or a HEXAGON.',
    type = int
)

# pars_args checks the command line input and converts each argument to the appropriate type.
# It returns a tuple of all arguments and their values.
args = parser.parse_args()
print(args)

# The following lines define the behavior of the python module based on the CL arguments.
# If an argument was not called, then it defaults to None.
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
