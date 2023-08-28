import math
class Triangle:
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
    def InputInfo(self):
        self.a = float(input("Nhap canh a: "))
        self.b = float(input("Nhap canh b: "))
        self.c = float(input("Nhap canh c: "))
    def chuvi(self):
        return self.a + self.b +self.c
    def dientich(self):
        return 0
class rightTriangle(Triangle):
    def __init__(self) -> None:
        super().__init__()
    def InputInfo(self):
        return super().InputInfo()
    def chuvi(self):
        return super().chuvi()
    def dientich(self):
        return (1/2) * self.a * self.b
class isoscelesTriangle(Triangle):
    def __init__(self) -> None:
        super().__init__()
    def InputInfo(self):
        return super().InputInfo()
    def chuvi(self):
        return super().chuvi() 
    def dientich(self):
        p = self.chuvi()/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) 
class equilateralTriangle(isoscelesTriangle):
    def __init__(self) -> None:
        super().__init__()
    def InputInfo(self):
        return super().InputInfo()
    def chuvi(self):
        return super().chuvi()
    def dientich(self):
        return super().dientich()

a = rightTriangle()
a.InputInfo()

b = isoscelesTriangle()
b.InputInfo()

c = equilateralTriangle()
c.InputInfo()

print(f"Chu vi va dien tich cua tam giac vuong la: {a.chuvi()}, {a.dientich()}")
print(f"Chu vi va dien tich cua tam giac vuong la: {b.chuvi()}, {b.dientich()}")
print(f"Chu vi va dien tich cua tam giac vuong la: {c.chuvi()}, {c.dientich()}")

