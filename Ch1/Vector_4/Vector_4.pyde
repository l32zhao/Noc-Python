from PVector import *

def setup():
#     global location, velocity
#     location = PVector(100, 100)
#     velocity = PVector(2.5, 5)
    size(640, 320)
#     stroke(0)
    background(255)

def draw():
    background(255)
    
    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)
    
    # 1.add
    #
    
    # 2.sub
    mouse.sub(center)
    
    
    # # 3.mult
    # mouse.mult(3)
    
    # # 4.div
    # mouse.div(6)
    
    # 5.mag
    m = mouse.mag()
    # print(m)
    fill(0)
    rect(0,0,m,10)
    
    # # 6.norm
    # mouse.norm()
    # mouse.mult(50)
    
    translate(width/2, height/2)
    line(0,0,mouse.x,mouse.y)
