from packages.shapies import Shape
import math
    
class Triangle(Shape):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

    def compute_area(self):
        a=0
        for const in range(len(self.edges)):
            a+=(self.edges[const]).compute_lenght()
        self.perimeter=a
        s=(self.perimeter)/2
        self.area=math.sqrt(s*(s-((self.edges[0]).compute_lenght()))*(s-((self.edges[1]).compute_lenght()))*(s-((self.edges[2]).compute_lenght())))
        return self.area

    def compute_inner_angles(self):
        a = self.edges[0].compute_lenght()
        b = self.edges[1].compute_lenght()
        c = self.edges[2].compute_lenght()
        angle_alpha = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_beta = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_gamma = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
        self.inner_angles = [angle_alpha, angle_beta, angle_gamma]
        return self.inner_angles

class Iscoceles(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)


class Equilateral(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
        self.inner_angles=[60]*3

class Scalene(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)

class Rectangle(Triangle):
    def __init__(self,edges,vertices):
        super().__init__(edges,vertices)
