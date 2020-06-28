import random
import numpy as np
import scipy.stats as st

def fn():
    a = random.randint(0, 10)
    while a<5:
        a = random.randint(0,10)
    print(f"第一种Random：{a}")

    b = np.random.randint(1, 10)
    while b <5:
        b = np.random.randint(1, 10)
    print(f"第二种Numpy：{b}")

    c = st.poisson.rvs(mu=20, size=[1])
    while c <5:
        c = st.poisson.rvs(mu=20, size=[1])
    print(f"第三种Scipy：{c[0]}")




fn()