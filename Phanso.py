class phanso():
    def __init__(self, tuso =0 , mauso = 0) -> None:
        self.tuso = tuso
        self.mauso = mauso
    def get(self):
        return self.tuso, self.mauso
    def set(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso
    def inputInfo(self):
        self.tuso = int(input())
        self.mauso = int(input())
        while self.mauso == 0:
                print("Nhap lai mau so: ")
                self.mauso = int(input())
    def UCLN(self,a,b):
        while b != 0:
            temp = a%b
            a = b
            b = temp
        return a
    def printInfo(self):
        print(self.tuso, "/", self.mauso)
    def rutgon(self):
        ucln = self.UCLN(self.tuso, self.mauso)
        self.tuso = self.tuso / ucln
        self.mauso = self.mauso / ucln
        return self.tuso, self.mauso
    def reverse(self):
        if self.tuso == 0:
            print("Khong the nghich dao")
        else:
            a = self.tuso
            self.tuso = self.mauso
            self.mauso = a
            return self.tuso, self.mauso
    def add(self, tuso2, mauso2):
        tumoi= self.tuso * mauso2 + tuso2 * self.mauso
        maumoi = self.mauso * mauso2
        return phanso(tumoi, maumoi)
    def sub(self, tuso2, mauso2):
        tumoi = self.tuso * mauso2 - tuso2 * self.mauso
        maumoi = self.mauso * mauso2
        return phanso(tumoi, maumoi)
    def multi(self, tuso2, mauso2):
        tumoi = self.tuso * tuso2
        maumoi = self.mauso * mauso2
        return phanso(tumoi, maumoi)
    def div(self, tuso2, mauso2):
        tumoi = self.tuso * mauso2
        maumoi = self.mauso * tuso2
        return phanso(tumoi, maumoi)
ps = phanso()
ps2 = phanso()
ps.inputInfo() 
ps2.inputInfo()
tong = ps.add(ps2.tuso, ps2.mauso)
tong.rutgon()
tong.printInfo()
hieu = ps.sub(ps2.tuso, ps2.mauso)
hieu.rutgon()
hieu.printInfo()
tich = ps.multi(ps2.tuso, ps2.mauso)
tich.rutgon()
tich.printInfo()
thuong = ps.div(ps2.tuso, ps2.mauso)
thuong.rutgon()
thuong.printInfo()
        