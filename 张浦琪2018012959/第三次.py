import random
import pymongo
clicent = pymongo.MongoClient()
db = clicent.person
number = db.number
def RandomInt(a,b,c,d):
    for i in range(10):
       ran=random.randint(a,b)
       if c<=ran<=d:
            yield ran

def RandomFloat(a,b,c,d):
    for i in range(10):
        ran = random.uniform(a, b)
        if c <= ran <= d:
            yield ran

def RandomStr():
    str='abcdefghijklmnopqrstuvwxyz!@#$%^&*()'
    for i in range(10):
        ch = random.choice(str)
        if 'a' <= ch <= 'z':
            yield ch

random1=RandomInt(1,100,5,20)
random2=RandomFloat(1,100,5,20)
random3=RandomStr()
randomlist = []
for j in random1:
    randomlist.append({"num1":j})
for j in random2:
    randomlist.append({"num2":j})
for j in random3:
    randomlist.append({"num1":j})
number.insert(randomlist)
def get_by_momngodb_select():
    # 查询所有的数据
    num_list = number.find()
    new_num_list = []
    for s in num_list:
        if s.get("num1"):
            new_num_list.append(s.get("num1"))
        elif s.get("num2"):
            new_num_list.append(s.get("num2"))
        elif s.get("num3"):
            new_num_list.append(s.get("num3"))
    for t in new_num_list:
        if t%1==0:#区分整数
            number.insert({"re_num":t})
get_by_momngodb_select()