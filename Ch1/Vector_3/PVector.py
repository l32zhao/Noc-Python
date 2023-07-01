class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, velocity):
        self.x += velocity.x
        self.y += velocity.y
