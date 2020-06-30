import random
import string

def dataSampling(func):
  def wrapper(datatype, datarange, num, *conditions,strlen=8):
     try:    
      result=set()
      for index in range(1,num):
        if datatype is int:
            it=iter(datarange)
            item=random.randint(next(it),next(it))
            result.append(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.append(item)
            continue
        elif datatype is str:
            item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            continue
        else:
            continue
     return func(result, *conditions)
    return wrapper
@dataSampling
def dataScreening():
  result=set()
  try:
    for a in data:
            if type(a) is int or type(a) is float:
                it = iter(range)
                if next(it) <= j <= next(it):
                    result.add(a)
            elif type(a) is str:
                for arr in range:
                    if arr in a:
                        result.add(a)
return result
def apply():
    result=dataScreening(int, (1, 20), 10, 5 , 15)
    print(result)
    result=dataScreening(float, (1, 20), 10, 5, 15)
    print(result)
    result=dataScreening(str, string.ascii_letters + string.digits, 20, 'a')
    print(result)

apply()