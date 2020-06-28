import random
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["runoobdb"]
mycol = mydb["hk"]


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
    if rd_type == 'int':
        for i in range(rd_num):
            item = random.randint(1, rd_range)
            print(item)
            mydict = {"data": item}
            mycol.insert_one(mydict)


    if rd_type == 'float':
        for i in range(rd_num):
            item = random.random() * rd_range
            print(item)
            mydict = {"data": item}
            mycol.insert_one(mydict)


    if rd_type == 'str':
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        for i in range(rd_num):
            s = ''
            for j in range(rd_range):
                s += random.choice(seed)
            item = s
            mydict = {"data": item}
            mycol.insert_one(mydict)


def dataScreening():
    if rd_type == 'int' or rd_type == 'float':
        print("请输入数据的筛选范围：")

        rd_screen.append(int(input()))
        rd_screen.append(int(input()))
        print("筛选范围：")
        print(rd_screen)
        print("筛选出的数据为：")

        for i in mycol .find({"$lte": rd_screen[1], "$gte": rd_screen[0]}):
            print(i["data"])


    elif rd_type == 'str':
        print("请输入您希望筛选出的最小首字母：")
        rd_screen.append(input())
        print("筛选出的数据为：")

        for i in mycol.find({"data": {"$gte": rd_screen[0]}}):
            print(i["data"])


dataSampling()
dataScreening()
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")
