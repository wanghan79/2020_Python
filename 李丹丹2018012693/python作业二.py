import random
import functools

rd_str = set()
A_rd_str = set()
print("请输入数据类型：")
rd_type = input()
print("请输入数据范围：")
rd_range = int(input())  # int型&float型的数据范围：0到rd_range；  str型：rd_range是字符串长度
print("请输入数据个数：")
rd_num = int(input())  # 生成数据的个数
rd_screen = []


def dataSampling():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if rd_type == 'int':
                for i in range(rd_num):
                    rd_str.add(random.randint(1, rd_range))

            if rd_type == 'float':
                for i in range(rd_num):
                    rd_str.add(random.random() * rd_range)

            if rd_type == 'str':
                seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
                for i in range(rd_num):
                    s = ''
                    for j in range(rd_range):
                        s += random.choice(seed)
                    rd_str.add(s)
            print("随机生成的数据为：")
            print(rd_str)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@dataSampling()
def dataScreening():
    if rd_type == 'int' or rd_type == 'float':
        print("请输入数据的筛选范围：")
        rd_screen.append(int(input()))
        rd_screen.append(int(input()))
        print("筛选范围：")
        print(rd_screen)

        for item in rd_str:
            if rd_screen[1] >= item >= rd_screen[0]:
                A_rd_str.add(item)

    elif rd_type == 'str':
        print("您希望筛选出含有哪个字符串的str型数据：")
        rd_screen.append(input())

        for item in rd_str:
            if item.find(rd_screen[0]) != -1:
                A_rd_str.add(item)

dataScreening()
print("筛选出的数据为：")
print(A_rd_str)