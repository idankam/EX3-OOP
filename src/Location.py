class Location:

    def __init__(self, x=-1, y=-1, z=0):
        self.x = x
        self.y = y
        self.z = z

# copy
    def copy(self):
        new_loc = Location(self.x, self.y, self.z)
        return new_loc

# distance
    def distance(self, another_loc):
        dist = ((self.x - another_loc.x)^2 + (self.y - another_loc.y)^2 + (self.z - another_loc.z)^2) ^0.5
        return dist
