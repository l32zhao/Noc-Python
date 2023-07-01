from PVector import *

def setup():
    global p, velocity
    p = PVector(100, 100)
    velocity = PVector(2.5, 5)
    size(640, 320)
    stroke(0)
    background(255)

def draw():
    
    global p, velocity
    p.move(velocity)
    # print("yes")
    if ((p.location[0] > width) or (p.location[0] < 0)):
        velocity.location[0] = velocity.location[0] * -1
        # stroke(random(255))
        fill(random(175),random(175),random(175))
        background(random(255),random(255),random(255))
    if ((p.location[1] > height) or (p.location[1] < 0)):
        velocity.location[1] = velocity.location[1] * -1
        # stroke(random(255))
        fill(random(175),random(175),random(175))
        background(random(255),random(255),random(255))
    # fill(175)
    ellipse(p.location[0],p.location[1],36,36)
