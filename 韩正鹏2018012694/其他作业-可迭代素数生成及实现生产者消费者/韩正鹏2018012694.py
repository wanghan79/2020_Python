import random
'''
  Author:  ZhengPeng.Han
  Purpose: Using generators to generate prime numbers in any legal range.
  Created: 25/5/2020
'''
class PrimeNumbers:
    def __init__(self,start,end):   #在构造器中对PrimeNumbers这个类的start和end属性进行定义
        self.start=start            #start和end分别是素数生成的起始和终止位置
        self.end=end

    def isPrimeNum(self,k):         #定义一个判断是否为素数的函数
        if k<2:                     #最小素数是2，故2之前必没有素数
            return False
        for i in range(2,k):        #若k不被从2到k之间任意一个整数整除，则它就是素数
            if k%i==0:
                return False
        return True

    def __iter__(self):             #iter方法用于从起始到终止不断迭代
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k             #yield用于在迭代方法中输出判断为素数的值

re=set()
try:
    a=random.randint(0,10000)
    b=random.randint(0,10000)
    for x in PrimeNumbers(a,b):
        #print(x)
        re.add(x)
    if(not re):
        print("数据范围不合法，请重新输入")
    else:
        print("从",a,"到",b,"的素数有：",re)
except Exception as e:
    print(e)

