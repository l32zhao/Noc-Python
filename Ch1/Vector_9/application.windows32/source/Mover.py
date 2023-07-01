from PVector import *

class Mover:
    # location = new PVector()
    # velocity = new PVector()
    
    def __init__(self):
        self.location = PVector(width/2,height/2);
        self.velocity = PVector(0,0);
        self.acceleration = PVector(random(-0.01,0.01),random(-0.01,0.01));
        
        
    def update(self):
        self.acceleration = PVector(random(-1,1),random(-1,1));
        self.acceleration.mult(random(2));
        # self.acceleration.mult(noise(-2,2));    # Perlin Noise
        self.velocity.add(self.acceleration)
        self.velocity.limit(10)
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
    
    
