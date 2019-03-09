from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

        @abstractmethod
        def area(self):
            pass

class Square(Shapes):
    def area(self):
        return self.value * self.value

class Triangle(Shapes):
    def area(self):
        return self.value * self.value * 0.43

x = Square(10)
print('Square area ',x.area())
y = Triangle(3)
print('Triangle area ',y.area())
