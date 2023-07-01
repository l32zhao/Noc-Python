from PVector import *

def setup():
    global location, velocity
    location = PVector(100, 100)
    velocity = PVector(2.5, 5)
    size(640, 320)
    stroke(0)
    background(255)

def draw():
    background(255)
    global location, velocity
    location.add(velocity)
    # print("yes")
    if ((location.x > width) or (location.x < 0)):
        velocity.x = velocity.x * -1

    if ((location.y > height) or (location.y < 0)):
        velocity.y = velocity.y * -1

    fill(175)
    ellipse(location.x,location.y,36,36)
