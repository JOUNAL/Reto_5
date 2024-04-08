import math
class Shape:
    def __init__(self,edges,vertices):
        self.edges=edges
        self.vertices=vertices

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar calcular area()")
    
    def compute_perimeter(self):
        a=0
        for const in range(len(self.edges)):
            a+=(self.edges[const]).compute_lenght()
        self.perimeter=a
        return self.perimeter
    
    def compute_inner_angles(self):
        raise NotImplementedError("Subclases deben implementar calcular angulos internos()")
    
    def set_vertices(self, vertices):
        self.vertices=vertices
    
    def get_vertices(self):
        return self.vertices
    
    def set_edges(self, edges):
        self.edges=edges
    
    def get_edges(self):
        return self.edges
    
    def get_perimeter(self):
        return self.perimeter
    
    def get_inner_angles(self):
        return self.inner_angles

    
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
