import random
import numpy as np
import scipy.stats as st

def fn(f):
    a = random.randint(0, 10)
    while f(a)!=1:
        a = random.randint(0, 10)
        f(a)
    print(f"第一种Random：{a}")

    b = np.random.randint(1, 10)
    while f(b)!=1:
        b = np.random.randint(1, 10)
        f(b)
    print(f"第二种Numpy：{b}")

    c = st.poisson.rvs(mu=20, size=[1])
    while f(c) !=1:
        c = st.poisson.rvs(mu=20, size=[1])
        f(c)
    print(f"第三种Scipy：{c[0]}")
@fn
def prt(n):
    if n>5:
        return 1



