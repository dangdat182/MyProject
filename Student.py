class Student():
    def __init__(self) -> None:
        self.MSSV = ""
        self.DTB = ""
        self.tuoi = ""
        self.lop = ""
    def inputInfo(self):
        self.MSSV = input("MSSV: ")
        while not len(self.MSSV) ==8:
            print("Nhap lai MSSV: ")
            self.MSSV = input()
        self.DTB = float(input("DTB: "))
        while not (self.DTB >= 0 and self.DTB <= 10):
            print("Nhap lai DTB: ")
            self.DTB = float(input())
        self.tuoi = int(input("Tuoi: "))
        while not self.tuoi >= 18:
            print("Nhap lai tuoi: ")
            self.tuoi = int(input())
        self.lop = input("Lop: ")
        while not (self.lop.startswith('A') or self.lop.startswith('C')):
            print("Nhap lai lop: ")
            self.lop = input()
    def showInfo(self):
        print("MSSV la:", self.MSSV)
        print("DTB la:", self.DTB)
        print("Tuoi la:", self.tuoi)
        print("Lop la:", self.lop)
    def hocbong(self):
        if self.DTB >= 8:
            return True
hs1 = Student()
hs1.inputInfo()
hs1.showInfo()
if hs1.hocbong() == True:
    print("Ban da nhan duoc hoc bong!!!")
        