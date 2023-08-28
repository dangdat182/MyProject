class Sohoc():
    def __init__(self) -> None:
        self.number1 = 0
        self.number2 = 0
    def get(self):
        return self.number1, self.number2
    def set(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def inputInfo(self):
        self.number1 = int(input())
        self.number2 = int(input())
    def printInfo(self):
        print(self.number1)
        print(self.number2)
    def add(self):
        return self.number1 + self.number2
    def sub(self):
        return self.number1 - self.number2
    def multi(self):
        return self.number1 * self.number2
    def div(self):
        return self.number1 / self.number2
n= Sohoc()
n.inputInfo()
n.printInfo()
print("Tong hai so la: ", n.add())
print("Hieu hai so la: ", n.sub())
print("Tich hai so la: ", n.multi())
print("Thuong hai so la: ", float(n.div()))
