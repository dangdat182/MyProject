class nhanvien():
    def __init__(self) -> None:
        self.ten = ""
        self.tuoi = ""
        self.diachi = ""
        self.tienluong = ""
        self.giolam = ""
    def inputInfo(self):       
        self.ten = input("Ten: ")
        self.tuoi = int(input("Tuoi: "))
        self.diachi = input("Dia chi: ")
        self.tienluong = float(input("Tien luong: "))
        self.giolam = float(input("Gio lam: "))
    def printInfo(self):
        print("Ten cua nhan vien la: ", self.ten)
        print("Tuoi cua nhan vien la: ", self.tuoi)
        print("Dia chi cua nhan vien la: ", self.diachi)
        print("Tien luong cua nhan vien la: ", self.tienluong)
        print("Gio lam cua nhan vien la: ", self.giolam)
    def tinhThuong(self):
        if self.giolam >= 200:
            self.thuong = self.tienluong * 0.2
        elif self.giolam < 200 and self.giolam >= 100:
            self.thuong = self.tienluong * 0.1
        else:
            self.thuong = 0
        return self.thuong 
nhanvien1 = nhanvien()
nhanvien1.inputInfo()
nhanvien1.printInfo()
print("Tong so tien thuong cua nhan vien la: ",nhanvien1.tinhThuong())