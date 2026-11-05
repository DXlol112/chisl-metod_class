import math

def relative_error(approx,exact):
    return abs(approx - exact) / abs(exact)

def absolute_error(approx, exact):
    return abs(approx - exact)


values = [0.1] * 1_000_000
ordinary_sum = 0.0
for value in values:
    ordinary_sum += value

test_num = [
    ("Pi vs 3.14", 3.14, math.pi),
    ("0,1 + 0,2 vs 0.3", 0.1 +0.2, 0.3),
    ("manual sum mil 0.1 vs math.fsum", ordinary_sum, math.fsum(values))
]

for name, approx, exact in test_num:
    relative_x = relative_error(approx, exact)
    absolute_x = absolute_error(approx, exact)
    
    print(
        f"---- {name} -----\n"
        f"Приближённое: {approx}\n"
        f"Точное:       {exact}\n"
        f"Абсолютная погрешность: {absolute_x}\n"
        f"Относительная: {relative_x}"
    )

