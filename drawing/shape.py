"""This module contains the main functionality of the package - drawing a regular polygon.
"""

import turtle
import time

def draw_shape( angle_degrees, sides, length = 50, pen_color = 'black', sleep_time = 3):
    """
    Draws a regular polygon with a specified number of sides, angle degree, and optional
        length of the side, color of the pen and time for which the drawing remains on the screen.
    """
    pencil = turtle.Turtle()
    pencil.pen(pencolor = pen_color)
    for i in range(0, sides):
        pencil.fd(length)
        pencil.left(angle_degrees)
    time.sleep(sleep_time)
