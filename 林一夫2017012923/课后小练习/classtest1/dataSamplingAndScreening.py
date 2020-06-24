import string

from dataSampling import dataSampling
from dataScreening import dataScreening

result=list()

def Sampling(fn):
    # 定义一个嵌套函数
    def sampling(*args,**kwargs):
        global result
        result = dataSampling(str, string.ascii_letters, 1000, 10) + dataSampling(int, [0, 100], 1000) + dataSampling(
            float, [0, 100], 1000)
        fn(*args,**kwargs)
    return sampling

@Sampling
def Screening(ans,condition):
    for it in result:
        ans.add(dataScreening(it, condition))


