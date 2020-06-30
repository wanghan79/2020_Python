import random
import pymongo
import string
import json

client = pymongo.MongoClient('127.0.0.7', 27017)
db = client['db_test']
col = db['random_col']

def random_int(min, max, num):
    for i in range(num):
        yield random.choice(range(min, max))

def random_float(min, max, num):
    for i in range(num):
        yield random.uniform(min, max)

def random_str(slen, num):
    for i in range(num):
        yield ''.join([random.choice(string.ascii_letters + string.ascii_uppercase + string.digits) for _ in range(slen)])

def dec_persistence(filter_func):

    def wrap_func(*var_args):
        result = filter_func(*var_args)
        print("saving " + json.dumps(result) + " to mongo")
        col.insert(dict(value=result))

    return wrap_func

@dec_persistence
def filter(generator, min, max):

    result =  [r for r in generator]

    if type(result[0]) is int:
        return [x for x in result if min < x < max]

    elif type(result[0]) is float:
        return [x for x in result if min < x < max]

    elif type(result[0]) is str:
        return [x for x in result if x.find(min) > -1 and x.find(max) > -1]

    else:
        raise "internal exception"

def main():
    int_generator = random_int(1, 1000, 10)
    print(filter(int_generator, 200, 700))

    fl_generator = random_float(1, 10000, 30)
    print(filter(fl_generator, 20, 5000))

    str_generator = random_str(8, 10)
    print(filter(str_generator, 'a', 'a'))


if __name__ == "__main__":
    main()

