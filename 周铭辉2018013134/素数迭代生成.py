"""

姓名: 周铭辉    学号：2018013134
项目实践作业   （1，10000）范围内查找打印素数


"""
class PrimesNum:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimes(self, item):
        if item <= 1:
            return False
        for y in range(2, item):
            if item % y == 0:
                return False
        return True

    def __iter__(self):
        self.it = self.start
        return self

    def __next__(self):
        for item in range(self.it, self.end):
            if self.isPrimes(item):
                self.it = item + 1
                return item
        raise StopIteration

print([x for x in PrimesNum(1, 10000)])