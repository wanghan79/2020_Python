'''
Description:
本次作业内容：
1. 使用两个函数分别封装随机数生成和数据筛选功能。
2. 随机数生成函数至少支持整型、浮点型和字符串类型，数据类型、数据范围和数据个数等信息以输入参数方式传入函数。实现过程要求先判断数据类型再完成相应随机数生成，采用异常处理机制保证代码健壮性。
3. 数据筛选函数至少支持整型、浮点型和字符串类型，待筛选数据和筛选条件均作为参数传入，采用异常处理机制保证代码健壮性。
4. 调用上述封装函数进行测试，包括各种类型的随机数生成，然后给出多种条件进行筛选
5.随机数生成函数使用生成器
6.使用MongoDB存储rangedata_creat中生成的随机数，并能从MongoDB中查询数据进行数据筛选。
Author：yuye.Dong
purpose:Generate random data set
Created:25/6/2020

'''
import random
import string
import pymongo





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

       # print(L)


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
    chars = string.ascii_letters + string.digits

    ''':Description:test.'''
    #MONGO操作
    # 创建库

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist = myclient.list_database_names()  # 查找数据库是否存在
    if "ll_data" in dblist:
        print("ll_data already have")
    mydb = myclient["ll_data"]  # 有就返回指针 没有就新建
    # 创建集合
    collist = mydb.list_collection_names()
    if "data_int" in collist:
        print("int already have")

    myint = mydb["data_int"]
    if "data_string" in collist:
        print("string already have")

    mystring = mydb["data_string"]
    if "data_float" in collist:
        print("float already have")

    myfloat = mydb["data_float"]

    # int work
    print('Test 1 about int:')
    result = []
    dataint = rangedata_creat(int, (0, 100), 23)
    for i in dataint:
        mydict = {"data": i}
        myint.insert_one(mydict)
    for x in myint.find():

        result.append(x.get("data"))
    print(result)
    print(data_select(result, 23, 34))
    print('\n')

    # floatwork
    result = []
    print('Test 2 about float:')
    datafloat = rangedata_creat(float, (1.00, 100.00), 20)
    for i in datafloat:
        mydict = {"data": i}
        myfloat.insert_one(mydict)
    for x in myfloat.find():
        #print(x.get("data"))
        #print(type(x.get("data")))
        result.append(x.get("data"))
    print(result)
    print(data_select(result, 20, 34))  #
    print('\n')

    # stringwork
    result = []
    print('Test3 about string:')
    datastring = rangedata_creat(string, chars, 100)
    for i in datastring:
        mydict = {"data": i}
        mystring.insert_one(mydict)
    for x in mystring.find():
        result.append(x.get("data"))
    print(result)
    print(data_select(result, 'T', 't'))
    print('\n')
    myint.delete_many({})
    myfloat.delete_many({})
    mystring.delete_many({})






apply()