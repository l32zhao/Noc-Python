class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, velocity):
        self.x += velocity.x
        self.y += velocity.y
        
    def sub(self, velocity):
        self.x -= velocity.x
        self.y -= velocity.y
        
    def mult(self, times):
        self.x *= times
        self.y *= times
    
    def div(self, times):
        self.x /= times
        self.y /= times
    
    def mag(self):
        return sqrt(self.x**2 + self.y**2)
    
    def norm(self):
        m = self.mag()
        if m != 0:
            self.div(m)
        else:
            self.x = 1
            self.y = 1

    def limit(self, topspeed):
        if self.mag() > topspeed:
            self.norm()
            self.mult(topspeed)
