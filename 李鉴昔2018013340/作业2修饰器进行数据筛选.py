"""
  Author:  jianxi.li
  Purpose: homework2:modify the random number filter function for data filtering;
  Created: 8/6/2020
"""
import random
import string
def datasampling(func):
    def wrapper(type, datarangement, quantity, *ans, strlen=15):
        output = list()
        if type is int:
            for item in range(0, quantity):
                options = iter(datarangement)
                document = random.randint(next(options), next(options))
                output.append(document)
        elif type is float:
            for item  in range(0, quantity):
                options = iter(datarangement)
                document = random.uniform(next(options), next(options))
                output.append(document)
        elif type is str:
            for item  in range(0, quantity):
                document = ''.join(random.SystemRandom().choice(datarangement) for _ in range(strlen))
                output.append(document)
        print('before:', output)
        return func(output, *ans)
    return wrapper




@datasampling
def dataScreening(datafile, *ans):
    output = list()
    for item  in datafile:
        if isinstance(item , int):
            if item  >= ans[0] and item  <= ans[1]:
                output.append(item )
        elif isinstance(item , float):
            if item  >= ans[0] and item  <= ans[1]:
                output.append(item )
        elif isinstance(item , str):
            flag = 1
            for x in item :
                if x not in ans[0]:
                    flag = 0
            if flag:
                output.append(item )
    print('later:', output)



dataScreening(int, [0, 100], 125, 0, 10)
dataScreening(float, [0, 100], 150, 0, 10)
dataScreening(str, string.ascii_letters + string.digits, 120, string.ascii_letters)

