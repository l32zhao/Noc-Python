from PVector import *

class Mover:
    # location = new PVector()
    # velocity = new PVector()
    
    def __init__(self):
        self.location = PVector(random(width),random(height));
        self.velocity = PVector(random(-2,2),random(-2,2)); 
        
    def update(self):
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
        fill(175)
        ellipse(self.location.x,self.location.y,16,16)
    
    
