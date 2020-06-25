import random

A_rd_str = set()
print("请输入数据类型：")
rd_type = input()
print("请输入数据范围：")
rd_range = int(input())  # int型&float型的数据范围：0到rd_range；  str型：rd_range是字符串长度
print("请输入数据个数：")
rd_num = int(input())  # 生成数据的个数
rd_screen = []

def dataSampling():
    if rd_type == 'int':
        for i in range(rd_num):
            item = random.randint(1, rd_range)
            yield item

    if rd_type == 'float':
        for i in range(rd_num):
            item = random.random() * rd_range
            yield item

    if rd_type == 'str':
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        for i in range(rd_num):
            s = ''
            for j in range(rd_range):
                s += random.choice(seed)
            item = s
            yield item


def dataScreening():
    if rd_type == 'int' or rd_type == 'float':
        print("请输入数据的筛选范围：")
        rd_screen.append(int(input()))
        rd_screen.append(int(input()))
        print("筛选范围：")
        print(rd_screen)

        for x in rd_str:
            if rd_screen[1] >= x >= rd_screen[0]:
                print(x)
                A_rd_str.add(x)


    elif rd_type == 'str':
        print("您希望筛选出含有哪个字符串的str型数据：")
        rd_screen.append(input())

        for x in rd_str:
            if x.find(rd_screen[0]) != -1:
                A_rd_str.add(x)


rd_str = dataSampling()
dataScreening()
print("筛选出的数据为：")
print(A_rd_str)