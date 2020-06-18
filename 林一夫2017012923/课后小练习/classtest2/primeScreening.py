class PrimeNumbers:
    def __init__(self,start,end):
        self.sart=start;
        self.end=end;

    def isPrimeNum(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        return True

    def __iter__(self):
        for k in range(self.sart,self.end):
            if self.isPrimeNum(k):
                print('数据范围由%d到%d' %(self.sart,self.end))
                yield k

for x in PrimeNumbers(1,100):
    print(x)
