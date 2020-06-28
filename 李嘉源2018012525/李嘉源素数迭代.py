"""
姓名：李嘉源 学号：2018012525
项目实践作业  素数迭代生成
"""
import random
#打印0 10000 一万素数
import math
def isPrimes1(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def q4():
    for elem in range(0,10000):
        if isPrimes1(elem):
            print(elem)
if __name__ == '__main__':
    q4()