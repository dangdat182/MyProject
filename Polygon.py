class polygon():
    def __init__(self) -> None:
        self.socanh = 0
        self.canh = []
    def nhapcanh(self):
        self.socanh = int(input("Nhap so canh: "))
        print("Nhap canh theo chieu dai giam dan:")
        for i in range(self.socanh):
            canh = float(input(f"Nhap canh thu {i+1}: "))
            self.canh.append(canh)
    def chuvi(self):
        return sum(self.canh)
    def dientich(self):
        raise NotImplementedError("Phuong thuc dien tich chua duoc xac dinh")
class parallelogram(polygon):
    def nhapcanhparalell(self):
        print("Hinh binh hanh: ")
        polygon.nhapcanh(self)
        self.chieucao = float(input("Nhap chieu cao: "))
    def dientich(self):
        day = self.canh[0]
        return day * self.chieucao
class retangle(parallelogram):
    def nhapcanhretangle(self):
        print("Hinh chu nhat: ")
        polygon.nhapcanh(self)
    def dientich(self):
        return self.canh[0] * self.canh[2]
class square(retangle):
    def nhapcanhsquare(self):
        print("Hinh vuong: ")
        polygon.nhapcanh(self)
    def dientich(self):
        return self.canh[0] ** 2
    
hbh = parallelogram()
hbh.nhapcanhparalell()

hcn = retangle()
hcn.nhapcanhretangle()

hv = square()
hv.nhapcanhsquare()

print("Chu vi hinh binh hanh la:", hbh.chuvi())
print("Dien tich hinh binh hanh la:", hbh.dientich())

print("Chu vi hinh chu nhat la:", hcn.chuvi())
print("Dien tich hinh chu nhat la:", hcn.dientich())    
         