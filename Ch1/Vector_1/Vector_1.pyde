# from pyprocessing import *
width = 640
height = 360

def setup():
    global x, y, xspeed, yspeed
    size(640,360)
    background(255)

    x = 100
    y = 100
    xspeed = 1
    yspeed = 3.3

def draw():
    global x, y, xspeed, yspeed
    background(255)
    
    x += xspeed
    y += yspeed
    # print("yes",x,y)
    
    if x > width or x < 0:
        xspeed *= -1

    if y > height or y < 0:
        yspeed *= -1
    
    stroke(0)
    fill(175)
    ellipse(x,y,16,16)
