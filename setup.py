from setuptools import setup

setup(
    name='drawing',
    version='0.1',
    description='A package which draws right polygons.',
    long_description='The package can draw any kinds of a right polygon on the whiteboard.',
    url='https://github.com/eliyanovva/turtle-argparse-example',
    author='Tedy',
    author_email='tedy@example.com',
    license='MIT',
    packages=['drawing'],
    install_requires=[
        'turtle', 'argparse'
    ],
    entry_points={
        'console_scripts': ['draw=drawing.draw_shapes:draw'],
    },
    scripts=['bin/draw-square', 'bin/circle']
)