
def myprime(x):#判断一个数x是否为素数


    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def myprimes(v):
    for i in range(v):
        if myprime(i):
            yield i



for x in myprimes(45):
    print(x)