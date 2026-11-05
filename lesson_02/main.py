import math, mpmath

mpmath.mp.dps = 60

def experiment(f_bad, f_good, xs, f_exact):
    print(f"{'x':>10} | {'bad':>14} | {'good':>14} | "
          f"{'err_bad':>10} | {'err_good':>10}")
    print("-" * 78)
    for x in xs:
        b  = f_bad(x)
        g  = f_good(x)
        ex = f_exact(x)
        eb = abs(b - ex) / abs(ex)
        eg = abs(g - ex) / abs(ex)
        print(f"{x:>10.0e} | {b:>14.8e} | {g:>14.8e} | "
              f"{eb:>10.2e} | {eg:>10.2e}")


x_small = [1e-10, 1e-6, 1e-4, 1e-2, 1]
x_medium = [10**2, 10**4, 10**6]
x_big = [10**10, 10**12, 10**14]
experiment(
    f_bad=lambda x: math.sqrt(x + 1) - math.sqrt(x),
    f_good=lambda x: 1 / (math.sqrt(x + 1) + math.sqrt(x)),
    xs=x_small + x_medium + x_big,
    f_exact=lambda x: mpmath.sqrt(mpmath.mpf(x) + 1) - mpmath.sqrt(x),
)
