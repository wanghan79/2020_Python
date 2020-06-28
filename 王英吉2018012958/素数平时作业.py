class PrimeNumbers:
    def __init__(self,q,p):
        self.q=q
        self.p=p
    def __iter__(self):
        for m in range(self.q,self.p):
            if self.isPrimeNum(m):
                yield m
    def isPrimeNum(self,m):
        if m<2:
            return False
        for n in range(2,m):
            if m%n==0:
                return False
        return True
for a in PrimeNumbers(1,10000):
    print(a)