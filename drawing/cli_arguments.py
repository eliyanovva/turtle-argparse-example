import argparse

class DrawingParser(argparse.ArgumentParser):
    def __init__(self):
         super().__init__(
            description='Use this module to print a regular polygon with any number of sides!',
            epilog='Thanks for stopping by!'
        )
    
    def setup_arguments(self):
        self.add_argument(
            '--big', help = 'Makes the side of the shape 100 pixels.', action = 'store_true'    
        )
        self.add_argument(
            '--small', help = 'Makes the side of the shape 30 pixels.', action = 'store_true'
        )
        self.add_argument(
            '--length', help = 'Sets the length of the side of a shape to a custom value.', type = int
        )
        self.add_argument(
            '--pen-color', help = 'Sets the color of the pen to a given color.'
        )
        self.add_argument(
            '--time',
            help = 'Sets the time to wait after the shape is completed in seconds, defaults to 3 seconds.',
            type = int
        )
        self.add_argument(
            'sides',
            help = 'Specifies the the number of sides of the polygon to be drawn.',
            type = int
        )