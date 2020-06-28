import random

class work_1(object):
    def __init__(self):
        self.rd_str = set()
        self.A_rd_str = set()

    def dataSampling(self, rd_type, rd_range, rd_num):
        if rd_type == 'int':
            for i in range(rd_num):
                self.rd_str.add(random.randint(1, rd_range))

        if rd_type == 'float':
            for i in range(rd_num):
                self.rd_str.add(random.random() * rd_range)

        if rd_type == 'str':
            seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
            for i in range(rd_num):
                s = ''
                for j in range(rd_range):
                    s += random.choice(seed)
                self.rd_str.add(s)
        print("随机生成的数据为：")
        print(self.rd_str)

    def dataScreening(self, rd_type, rd_screen):
        if rd_type == 'int' or rd_type == 'float':
            for item in self.rd_str:
                if rd_screen[1] >= item >= rd_screen[0]:
                    self.A_rd_str.add(item)
        else:
            for item in self.rd_str:
                if item.find(rd_screen[0]) != -1:
                    self.A_rd_str.add(item)
        rd_screen.clear()

    def main_con(self):
        print("请输入数据类型：")
        rd_type = input()
        print("请输入数据范围：")
        rd_range = int(input())      # int型&float型的数据范围：0到rd_range；  str型：rd_range是字符串长度
        print("请输入数据个数：")
        rd_num = int(input())        # 生成数据的个数
        self.dataSampling(rd_type, rd_range, rd_num)

        rd_screen = []
        if rd_type == 'int' or rd_type == 'float':
            print("请输入数据的筛选范围：")
            rd_screen.append(int(input()))
            rd_screen.append(int(input()))
            print("筛选范围：")
            print(rd_screen)

        elif rd_type == 'str':
            print("您希望筛选出含有哪个字符串的str型数据：")
            rd_screen.append(input())

        self.dataScreening(rd_type, rd_screen)
        print("筛选出的数据为：")
        print(self.A_rd_str)


if __name__ == "__main__":
    test = work_1()
    test.main_con()