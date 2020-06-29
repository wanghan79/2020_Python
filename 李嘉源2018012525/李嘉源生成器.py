"""
姓名：李嘉源 学号：2018012525
项目实践第三次作业  Generate random data set with generator.
"""
#用生成器生成list，并进行过滤
import random

#生成器
def dataSampling2(type,min,max,N):
    if N<=0:

        print('please input the correect N(>0)')
    else:
        if type in ['int','float']:

            if max>min:
                if type=='int':
                    L=[elem2 for elem2 in [random.randint(min, max) for item in range(N)]]
                if type=='float':
                    L = [elem2 for elem2 in [random.uniform(min, max) for item in range(N)]]
                return L
            else:
                print('min max error')
        else:
            print('type error')


#改成生成器
def dataScreening2(data,flag1,flag2):
    elem=data[0]
    print('type is {}'.format(type(elem)))
    L = [elem2 for elem2 in data if elem2>=flag1 and elem2<=flag2]

    return L


def apply2():

    print('test   on  int ')
    test1=dataSampling2('int',0,100,50)
    print('随机生成10个 0 到100 的数字')
    print(test1)

    #过滤
    test1 = dataScreening2(test1, 50, 60)
    print('筛选50 到 60 区间的数字')
    print(test1)

    print('test   on  float ')
    test2 = dataSampling2('float', 0, 100, 50)
    print('随机生成10个 0 到100 的数字')
    print(test2)

    # 过滤
    test1 = dataScreening2(test2, 50, 60)
    print('筛选50 到 60 区间的数字')
    print(test2)




if __name__ == '__main__':

   apply2()