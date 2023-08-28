class matrix():
    def __init__(self) -> None:
        self.row = 0
        self.col = 0
        self.data = [[0] * self.col for _ in range(self.row)]
    def set(self, row, col, value):
        self.data[row][col]= value
    def get(self, row, col):
        return self.data[row][col]
    def inputInfo(self):
        row = int(input("Nhap so dong: "))
        col = int(input("Nhap so cot: "))
        for i in range(row):
            for y in range(col):
                n = float(input())
                self.data.append(n)
    def printInfo(self):
        for row in self.data:
            print(row)
mt= matrix()
mt.inputInfo()
mt.printInfo()