from PVector import *
from Mover import *

movers = []

def setup():
    size(1024, 360)
    for i in range(20):
        movers.append(Mover()) 

def draw():
    background(255)
    for i in range(len(movers)):
        movers[i].update()
        # movers[i].checkEdges()
        movers[i].display()
