import math
class Points():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def InputInfo1(self):
        self.x = float(input())
        self.y = float(input())
    def Dientich(self):
        return 0
class Ellipse(Points):
    def __init__(self) -> None:
        super().__init__()
    def InputInfo(self):
        print("Nhap toa do tam hinh ellipse: ")
        super().InputInfo1()
        self.a = float(input("Nhap chieu dai truc lon: "))
        self.b = float(input("Nhap chieu dai truc nho: "))
    def Dientich(self):
        return math.pi * self.a * self.b
class Circle(Ellipse):
    def __init__(self) -> None:
        super().__init__()
    def InputInfo(self):
        print("Nhap toa do tam hinh tron: ")
        super().InputInfo1()
        self.a = float(input("Nhap duong kinh: "))
    def Dientich(self):
        return math.pi * (self.a)**2
circle = Circle()
circle.InputInfo()


elip = Ellipse()
elip.InputInfo()

print(f"Dien tich hinh tron la: {circle.Dientich()}")
print(f"Dien tich hinh ellipse la: {elip.Dientich()}")