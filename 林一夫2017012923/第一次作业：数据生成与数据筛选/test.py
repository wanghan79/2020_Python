import string

from dataSampling import dataSampling
from dataScreening import dataScreening

result=dataSampling(str,string.ascii_letters,1000,10)

ans=set()
for it in result:
    ans.add(dataScreening(it,'ab'))
print(ans)
