'''
Description:
本次作业内容：
1. 使用两个函数分别封装随机数生成和数据筛选功能。
2. 随机数生成函数至少支持整型、浮点型和字符串类型，数据类型、数据范围和数据个数等信息以输入参数方式传入函数。实现过程要求先判断数据类型再完成相应随机数生成，采用异常处理机制保证代码健壮性。
3. 数据筛选函数至少支持整型、浮点型和字符串类型，待筛选数据和筛选条件均作为参数传入，采用异常处理机制保证代码健壮性。
4. 调用上述封装函数进行测试，包括各种类型的随机数生成，然后给出多种条件进行筛选

Author：yuye.Dong
purpose:Generate random data set
Created:15/5/2020

'''
import random
import string

#数据生成
def rangedata_creat(dtype, drange_low,drange_high, dnum,strlen=10):
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

            L = [random.randint(drange_low,drange_high) for _ in range(dnum)]



        elif dtype is float:
            L = [random.uniform(drange_low,drange_high)for _ in range(dnum)]


        elif dtype is string:
            L = [''.join(random.sample(chars, strlen)) for _ in range(dnum)]  # 列表转字符串




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

    print('Test 1:')
    #test int
    S = rangedata_creat(int,0,100, 23)

    print('生成int型随机数：')
    print(S)
    print(data_select(S,23,34))#筛选范围为20-34的数
    print('\n')
    #test float
    print('Test 2:')
    S = rangedata_creat(float,1.00,100.00,23)
    print('生成float型随机数：')
    print(S)
    print( data_select(S,20.00,34.00))#筛选范围为20-34的浮点数
    print('\n')

    #test string
    print('Test3:')
    S = rangedata_creat(string,chars,chars, 20)#生成20个长度为10的字符串
    print('生成随机字符串：')
    print(S)
    print(data_select(S,'T','t'))#筛选带有't'和'T'的字符串






apply()