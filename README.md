# Turtle & Argparse Package
This simple package of Python CLI aliases and the Python argparse library was created as a demo for my team during my internship in Festo.

## Installation
To use the package, you would need Python 3.x. It is best to use a Python virtual environment to install it. I used *pipenv*; detailed instructions for the isntallation of *pipenv* can be found here: https://www.pythontutorial.net/python-basics/install-pipenv-windows/. A workflow of how to use *pipenv* to install the package can be found here: https://pipenv-fork.readthedocs.io/en/latest/basics.html

Installation
```bash
git clone https://github.com/eliyanovva/turtle-argparse-example
cd turtle-argparse-example
pipenv install

```
## Function
The package will print regular polygons on the screen, using the *turtle* Python package. They can vary in number of sides, side-length, and border color. To see the possible inputs, run the following command:
```bash
draw -h
Use this module to print a regular polygon with any number of sides!

positional arguments:
  sides                 Specifies the the number of sides of the polygon to be drawn.

optional arguments:
  -h, --help            show this help message and exit
  --big                 Makes the side of the shape 100 pixels.
  --small               Makes the side of the shape 30 pixels.
  --length LENGTH       Sets the length of the side of a shape to a custom value.
  --pen-color PEN_COLOR
                        Sets the color of the pen to a given color.
  --time TIME           Sets the time to wait after the shape is completed in seconds, defaults to 3 seconds.

Thanks for stopping by!
```
 
 
