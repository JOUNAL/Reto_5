from packages.shapies import Shape
import math

class Rectangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)

    def compute_area(self):
        a=1
        for const in range(len(self.edges)):
            a*=(self.edges[const]).compute_lenght()
        self.area=math.sqrt(a)
        return self.area

class Square(Rectangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=([90]*4)
