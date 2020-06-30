 ##!E/Python tird-homework
"""
    Author:
        BowenCao
        2018013070

    Purpose:
        Producer consumer issues

    Created: 30/5/2020
"""


def consumer(name):
    while True:
        result = yield
        print(name+"消费{}".format(result))
        print("休息5秒....")


def product():
    c1 = consumer("顾客c1: ")
    c2 = consumer("顾客c2: ")
    c1.__next__()
    c2.__next__()
    for i in range(10):
        print("生产{}".format(i))
        c1.send(i)
        c2.send(i)
    c1.close()
    c2.close()


product()