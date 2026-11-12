import math
import time

import numpy as np


class Template:
    def __init__(self, title, loop_fn, numpy_fn, *, inplace=False):
        self.title = title
        self.loop_fn = loop_fn
        self.numpy_fn = numpy_fn
        self.inplace = inplace

    def _measure(self, fn, arr):
        best = float("inf")
        for _ in range(3):
            result = None
            data = arr.copy() if self.inplace else arr
            t0 = time.perf_counter()
            result = fn(data)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def run(self, arr):
        r_loop, t_loop = self._measure(self.loop_fn, arr)
        r_numpy, t_numpy = self._measure(self.numpy_fn, arr)

        print(f"\n{self.title}")
        print(f"цикл:   {t_loop*1000:10.2f} мс")
        print(f"NumPy:  {t_numpy*1000:10.2f} мс")
        print(f"ускорение: {t_loop / t_numpy:.1f}×")
        print(f"результаты совпадают: {np.allclose(r_loop, r_numpy)}")
        return r_loop, r_numpy



rng = np.random.default_rng(42)
arr = rng.normal(size=1_000_000)


# Задача 1. 
def loop_sum(arr):
    total = 0.0
    for x in arr:
        total += x
    return total

def numpy_sum(arr):
    return arr.sum()

for n in (100_000, 1_000_000, 10_000_000):
    Template(f"1. Сумма (n = {n:_})", loop_sum, numpy_sum,).run(arr if n == arr.size else rng.normal(size=n))


# Задача 2.


# Задача 3.
def loop_transform(arr):
    result = []
    for x in arr:
        result.append(math.sin(x) + x * x)
    return result

def numpy_transform(arr):
    return np.sin(arr) + arr**2

Template("3. Поэлементное преобразование", loop_transform, numpy_transform).run(arr)


