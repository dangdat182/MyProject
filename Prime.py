class prime():
    def __init__(self,x) -> None:
        if self.isPrime(x) == True:
            self.__a = x
    def isPrime(self, x):
        if x == 1 or x == 2:
            return True
        else: 
            for i in range(2,x):
                if x%i == 0:
                    return False
                else:
                    return True
    def nextPrime(self): 
        nextnum = self.__a + 1
        while True:
            if self.isPrime(nextnum) == True:
                return nextnum
            nextnum +=1
    def get(self):
        return self.__a
    def set(self, x):
        if self.isPrime(x) == True:
            self.__a = x
        else:
            print("Khong set")  
sont = prime(5)
sont.set(2)