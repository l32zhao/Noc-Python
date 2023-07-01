class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
        
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
    
    @staticmethod      
    def sub2(v1, v2):
        return PVector(v1.x - v2.x, v1.y - v2.y)
    
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
