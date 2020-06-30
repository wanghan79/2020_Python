
__author__='2018013027'
import random
import string

def random_int(min, max, num):
    return [random.choice(range(min, max)) for _ in range(num)]

def random_float(min, max, num):
    return [random.uniform(min, max) for _ in range(num)]

def random_str(slen, num):
    return [''.join([random.choice(string.ascii_letters + string.ascii_uppercase + string.digits) for _ in range(slen)]) for x in range(num)]


def filter(result, min, max):
    if type(result) is not list or len(result) < 1:
        raise "bad result"

    if type(result[0]) is int:
        return [x for x in result if min < x < max]

    elif type(result[0]) is float:
        return [x for x in result if min < x < max]

    elif type(result[0]) is str:
        return [x for x in result if x.find(min) > -1 and x.find(max) > -1]

    else:
        raise "internal exception"

def main():
    result_int = random_int(1, 1000, 10)
    print("random int:")
    print(result_int)
    print(filter(result_int, 200, 700))

    result_fl = random_float(1, 2000,  10)
    print("random float:")
    print(result_fl)
    print(filter(result_fl, 0, 1000))

    result_str = random_str(8, 10)
    print("random str:")
    print (result_str)
    print(filter(result_str, 'm', 'nm'))

if __name__ == "__main__":
    main()






