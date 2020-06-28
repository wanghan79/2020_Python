import pymongo
import random
import numpy as np
import scipy.stats as st
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['datas']
p = db['data']

a = random.randint(0, 10)
while a<5:
    a = random.randint(0,10)
b = np.random.randint(1, 10)
while b <5:
    b = np.random.randint(1, 10)
c = st.poisson.rvs(mu=20, size=[1])
while c <5:
    c = st.poisson.rvs(mu=20, size=[1])

data = {
    'first':a,
    'sec':b,
    'third':c[0]
}
result = p.insert(data)
