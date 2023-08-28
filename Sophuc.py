class sophuc():
    def __init__(self, thuc = 0, ao = 0) -> None:
        self.thuc = thuc
        self.ao = ao
    def get(self):
        return self.thuc, self.ao
    def set(self, phanthuc, phanao):
        self.thuc = phanthuc
        self.ao = phanao
    def inputInfo(self):
        self.thuc = float(input())
        self.ao = float(input())
    def printInfo(self):
        if self.ao < 0:
            print(f"{self.thuc}{self.ao}i")
        elif self.ao == 0:
            print(f"{self.thuc}")
        elif self.ao > 0:
            print(f"{self.thuc}+{self.ao}i")
    def add(self, thuc2, ao2):
        thucmoi = self.thuc + thuc2
        aomoi = self.ao + ao2 
        return sophuc(thucmoi, aomoi)
    def sub(self, thuc2, ao2):
        thucmoi = self.thuc - thuc2
        aomoi = self.ao - ao2 
        return sophuc(thucmoi, aomoi)
    def multi(self, thuc2, ao2):
        thucmoi = self.thuc * thuc2 - self.ao * ao2
        aomoi = self.thuc * ao2 + self.ao * thuc2
        return sophuc(thucmoi, aomoi)
    def div(self, thuc2, ao2):
        thucmoi = (self.thuc * thuc2 + self.ao * ao2) / ((thuc2 ** 2) + (ao2 **2))
        aomoi = (thuc2 * self.ao - self.thuc * ao2) / ((thuc2 ** 2) + (ao2 **2))
        return sophuc(thucmoi, aomoi)
sophuc1 = sophuc()
sophuc2 = sophuc()

sophuc1.inputInfo()
sophuc2.inputInfo()

tong = sophuc1.add(sophuc2.thuc, sophuc2.ao)
tong.printInfo()

hieu = sophuc1.sub(sophuc2.thuc, sophuc2.ao)
hieu.printInfo()

tich = sophuc1.multi(sophuc2.thuc, sophuc2.ao)
tich.printInfo()

thuong = sophuc1.div(sophuc2.thuc, sophuc2.ao)
thuong.printInfo()
