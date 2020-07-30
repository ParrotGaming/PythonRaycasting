from math import pi
class Player:
    def __init__(self):
        self.x = 350
        self.y = 250
        self.fov = 2*pi/6
        self.angle = 0