"""
姓名：李嘉源 学号：2018012525
项目实践第二次作业  Generate random data set with Decorator.
"""

import  random
def q3():
    li2 = [elem2 for elem2 in [random.randint(-100, 100) for item in range(100)] if elem2 > 0]  ## 生成式返回给变量li的是一个生成器,通过[]将其转换成列表
    print('生成的随机数list：', li2)
    print('生成的随机数list长度：', len(li2))
    return li2

def filter(func,type,min,max,N):
    def wrapper():
        print('生成的随机数list：',func(type,min,max,N))
        print('生成的随机数list长度：', len(func(type,min,max,N)))
        return [elem for elem in func(type,min,max,N) if elem >50 ]  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper


#修饰器
def dataSampling3(type,min,max,N):
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


#修饰器方法
def dataScreening3(data,flag1,flag2):
    elem=data[0]
    print('type is {}'.format(type(elem)))
    L = [elem2 for elem2 in data if elem2>=flag1 and elem2<=flag2]

    return L


def apply3():
    print('test   on  int ')
    q2 = filter(dataSampling3, 'int', 0, 100, 50)
    L2 = q2()
    print('筛选后的数据为：', L2)
    print('筛选后的数据长度为：', len(L2))

    print('test   on  float ')
    q2 = filter(dataSampling3, 'float', 0, 100, 50)
    L2 = q2()
    print('筛选后的数据为：', L2)
    print('筛选后的数据长度为：', len(L2))


if __name__ == '__main__':
    apply3()