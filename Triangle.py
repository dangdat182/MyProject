from math import sqrt
class triangle():
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
    def inputInfo(self):
        print("Nhap 3 canh cua tam giac: ")
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())
    def type(self):
        if self.a == self.b == self.c:
            print("Tam giac deu")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Tam giac can")
        elif (self.a)**2 + (self.b)**2 == (self.c)**2 or (self.b)**2 + (self.c)**2 == (self.a)**2 or (self.a)**2 + (self.c)**2 == (self.b)**2:
            print("Tam giac vuong") 
        else:
            print("Tam giac thuong")
            
    def cv(self):
        return self.a + self.b + self.c
    def dt(self):
        p = (self.cv())/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
tamgiac = triangle()
tamgiac.inputInfo()
tamgiac.type()
print("Chu vi tam giac la:", tamgiac.cv()) 
print("Dien tich tam giac la:", tamgiac.dt())   