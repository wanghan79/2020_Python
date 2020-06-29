'''
Description:
本次作业内容：
1. 使用两个函数分别封装随机数生成和数据筛选功能。
2. 随机数生成函数至少支持整型、浮点型和字符串类型，数据类型、数据范围和数据个数等信息以输入参数方式传入函数。实现过程要求先判断数据类型再完成相应随机数生成，采用异常处理机制保证代码健壮性。
3. 数据筛选函数至少支持整型、浮点型和字符串类型，待筛选数据和筛选条件均作为参数传入，采用异常处理机制保证代码健壮性。
4. 调用上述封装函数进行测试，包括各种类型的随机数生成，然后给出多种条件进行筛选
5.随机数生成函数使用生成器
Author：yuye.Dong
purpose:Generate random data set
Created:15/6/2020

'''
import random
import string

#数据生成
def rangedata_creat(dtype, drange, dnum,strlen=10):
    '''
    :Description: Generate a given condition random data list.
    :param dtype: the datatype you want to sample including int, float, string.
    :param drange: iterable data list
    :param dnum: the number of data you need
    :return: a data list
    '''
    chars = string.ascii_letters + string.digits

    try:
        if dnum < 0:
            print("Please input correct num .")

        L = []
        if dtype is int:
            for i in range(0,dnum):
                it = iter(drange)
                item =random.randint(next(it),next(it))
                L.append(item)
                yield item

        elif dtype is float:
            for i in range(0, dnum):
                it = iter(drange)
                item = random.uniform(next(it), next(it))
                L.append(item)
                yield item


        elif dtype is string:
            for i in range(0, dnum):
                item = ''.join(random.SystemRandom().choice(drange) for _ in range(strlen))
                L.append(item)
                yield item
        print(L)


    except ValueError:
        print(" num error.")
    except NameError:
        print(" datatype Error.")
    except TypeError:
        print(" datatype Error.")
    except MemoryError:
        print("Maybe memory is full.")
    except:
        raise
    else:
        return L


#数据筛选
def data_select(L,*conditions):
    '''
        :Description: select out the right data in S
        :param dtype: the datatype you want to sample including int, float, string.
        :param S: the data list you have generated.
        :return: null
        '''
    selest2 = []

    try:
        for x in L:
            if type(x) is int:
                it = iter(conditions)
                if next(it) <= x and next(it) >= x:
                    selest2.append(x)

            elif type(x) is float:
                it = iter(conditions)
                if next(it) <= x and next(it) >= x:
                    selest2.append(x)

            elif type(x) is str:

                for digit in conditions:
                    if x.find(digit)==1:
                        selest2.append(x)

        return selest2


    except ValueError:
        print(" num error.")
    except NameError:
        print(" datatype Error.")
    except TypeError:
        print(" datatype Error.")
    except MemoryError:
        print("Maybe memory is full.")
    except:
        raise


    #except Exception as e:
        #print("default" + str(e))

#test
def apply():
    ''':Description:test.'''
    chars = string.ascii_letters + string.digits

    print('Test 1 about int:')
    #test int
    S = rangedata_creat(int,(0,100), 23)
    print(data_select(S,23,34))
    print('\n')
    #test float
    print('Test 2 about float:')
    S = rangedata_creat(float, (1.00,100.00),23)
    print( data_select(S,20,34))#
    print('\n')
    #test string
    print('Test3 about string:')
    S = rangedata_creat(string, chars, 100)
    print(data_select(S,'T','t'))
    print('\n')





apply()