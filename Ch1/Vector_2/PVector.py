class PVector:
    
    def __init__(self, x, y):
        self.location = [x,y]
    
    def move(self, velocity):
        self.location[0] += velocity.location[0]
        self.location[1] += velocity.location[1]
