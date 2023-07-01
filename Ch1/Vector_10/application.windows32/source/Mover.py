from PVector import *

class Mover:
    # location = new PVector()
    # velocity = new PVector()
    
    def __init__(self):
        self.location = PVector(random(width/2-50, width/2+50),random(height/2-50, height/2+50))
        global topspeed
        self.velocity = PVector(0,0)
        topspeed = 8
        self.color = [random(175,225),random(175,225),random(175,225)]
        
    def update(self):
        global velocity, topspeed
        mouse = PVector(mouseX, mouseY)
        dir = PVector.sub2(mouse, self.location)
        dir.norm()
        dir.mult(0.5)
        acceleration = dir

        self.velocity.add(acceleration)
        self.velocity.limit(topspeed)
        self.location.add(self.velocity)
    
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0 :
            self.location.x = width
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0 :
            self.location.y = height
    
    def display(self):
        stroke(0)
        # fill(100, 175)
        fill(self.color[0],self.color[1],self.color[2], 175)
        ellipse(self.location.x,self.location.y,48,48)
    
    
