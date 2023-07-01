from PVector import *
from Mover import *

def setup():
    size(640, 320)
    global mover
    mover = Mover()


def draw():
    background(255)
    global mover
    mover.update()
    mover.checkEdges()
    mover.display()
