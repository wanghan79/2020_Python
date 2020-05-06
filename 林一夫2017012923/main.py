import string

from dataSampling import dataSampling
from dataScreening import dataScreening


def apply():
    '''

    :return:
    '''
    ans=set()
    result=dataSampling(str,string.ascii_letters,1000,10)+dataSampling(int,[0,100],1000)+dataSampling(float,[0,100],1000)
    print(result)
    for it in result:
        ans.add(dataScreening(it,'at'))
    for it in result:
        ans.add(dataScreening(it,[10,50]))
    return ans

ans=apply()
print(ans)