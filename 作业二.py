import random
import string

def dec_filter(min, max):

    def wrap_outter(func):

        def wrap_inner(*var_args):

            result = func(*var_args)

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

        return wrap_inner

    return wrap_outter

@dec_filter(10, 500)
def random_int(min, max, num):
    return [random.choice(range(min, max)) for _ in range(num)]

@dec_filter(80000, 100000)
def random_float(min, max, num):
    return [random.uniform(min, max) for _ in range(num)]

@dec_filter('a', 'a')
def random_str(slen, num):
    return [''.join([random.choice(string.ascii_letters + string.ascii_uppercase + string.digits) for _ in range(slen)]) for x in range(num)]

def main():
    result_int = random_int(1, 1000, 10)
    print("random int:")
    print(result_int)

    result_fl = random_float(1, 1000000,  500)
    print("random float:")
    print(result_fl)

    result_str = random_str(8, 10)
    print("random str:")
    print (result_str)


if __name__ == "__main__":
    main()