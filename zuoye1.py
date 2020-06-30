import random
import string
import types
def zuoye1():
 print(random.uniform(10,20))#浮点型
 print(random.random())
 number=[]#列表收集随机数
 newlist=[]
 for i in range(0,100):#生成100个数以供筛选
  num = random.randint(0,500)#整型
  number.append(num)
 print(number)
#筛选大于200的数
 positive_list = [n for n in number if n > 200]
 print(positive_list)


