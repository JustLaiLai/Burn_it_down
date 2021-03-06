from abc import ABC, abstractmethod
import math
import unittest

class Shapes(ABC):
    def __init__(self, sides, size):
        self.size = size
        self.sides = sides
        super().__init__()

    def parameter(self):
        return self.sides * self.size
        
        @abstractmethod
        def area(self):
            pass

class Square(Shapes):
    def area(self):
        return self.size * self.size

class Triangle(Shapes):
    def area(self):
        return pow(self.size,2) * math.sqrt(3) / 4

#x = Square(4,10)
#print('Square area ',x.area())
#print('Square parameter ',x.parameter())
# = Triangle(3,3)
#print('Triangle area ',y.area(),' and its parameter',x.parameter())

