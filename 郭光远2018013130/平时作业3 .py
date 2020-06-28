import random
import numpy as np
import scipy.stats as st
def f():
    a = random.randint(0, 10)
    while a < 5:
        a = random.randint(0, 10)
    yield a
def s():
    b = np.random.randint(1, 10)
    while b < 5:
        b = np.random.randint(1, 10)
    yield b
def t():
    c = st.poisson.rvs(mu=20, size=[1])
    while c < 5:
        c = st.poisson.rvs(mu=20, size=[1])
    yield c[0]
def fn():
    t = f()
    print(f"第一种Random：{next(t)}")

    g = s()
    print(f"第二种Numpy：{next(g)}")

    p = s()
    print(f"第三种Scipy：{next(p)}")




fn()