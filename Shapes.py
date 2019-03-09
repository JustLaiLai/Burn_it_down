from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

        @abstractmethod
        def do_something(self):
            pass

class Dosmt(Shapes):
    def do_something(self):
        return self.value + 42

x = Dosmt(10)
print(x.do_something())
