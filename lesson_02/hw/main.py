import math
import random
from decimal import Decimal, localcontext
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend("Agg")

def absolute_error(approx, exact):
    return abs(approx - exact)


def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return absolute_error(approx, exact) / abs(exact)


def percentage_error(approx, exact):
    return relative_error(approx, exact) * 100


def task1():
    pairs = [("π", 3.14, math.pi), ("e", 2.718, math.e),
             ("g", 9.8, 9.81), ("1/3", 0.333, 1 / 3)]
    for name, approx, exact in pairs:
        print(f"{name}: Δx = {absolute_error(approx, exact):.8f}; "
              f"δx = {percentage_error(approx, exact):.6f}%")
    by_absolute = sorted(pairs, key=lambda p: absolute_error(p[1], p[2]))
    by_relative = sorted(pairs, key=lambda p: relative_error(p[1], p[2]))
    print("По Δx (от лучшего):", " → ".join(p[0] for p in by_absolute))
    print("По δx (от лучшего):", " → ".join(p[0] for p in by_relative))


def task2():
    pairs = [("Мост", 1247, 1250, "м"), ("Болт", 9.7, 10.0, "мм")]
    for name, approx, exact, unit in pairs:
        print(f"{name}: Δx = {absolute_error(approx, exact):g} {unit}; "
              f"δx = {percentage_error(approx, exact):g}%")


def task3():
    pairs = [(3.14, math.pi), (2.718, math.e), (9.8, 9.81), (0.333, 1 / 3)]
    for approx, exact in pairs:
        print(f"x = {approx:g}: δx = {relative_error(approx, exact):.8f}")
    print("exact = 0:", relative_error(10, 0))


def task4():
    x = 47.3
    delta = 0.1 / 100
    a = x / (1 + delta)
    b = x / (1 - delta)
    print("x* ∈ [47.3 / 1.001; 47.3 / 0.999]")
    print(f"Приближённо: [{a:.6f}; {b:.6f}]")


def task5():
    error_a = 0.3
    error_b = 0.5 / 100
    limit = error_a / error_b
    print(f"T ∈ [{-limit:g}; {limit:g}] °C")


def task6():
    numbers = ["0.004520", "1200", "1.200", "10.03", "0.03050", "250000"]
    for number in numbers:
        digits = number.replace(".", "").lstrip("0")
        count = len(digits)
        label = str(count)
        if "." not in number:
            count = len(digits.rstrip("0"))
            label = f"{count}–{len(digits)}"
        print(f"{number}: {label} значащих цифр; {float(number):.{count - 1}E}")
    print("Для 1200 и 250000 показана запись с 2 значащими цифрами.")


def task7():
    x = 4.738291
    delta = 0.02
    result = round(x, 2)
    print(f"x = {result:.2f} ± {delta:.2f}")
    print("Значащих цифр:", len(str(result).replace(".", "")))


def task8():
    print(round(0.5), round(1.5), round(2.5), round(3.5),
          round(-0.5), round(-1.5), round(-2.5))
    rng = random.Random(42)
    shift_up = 0.0
    shift_even = 0.0
    for _ in range(1_000_000):
        x = rng.randrange(10) + 0.5
        shift_up += math.floor(x + 0.5) - x
        shift_even += round(x) - x
    print(f"Сдвиг при округлении вверх: {shift_up:g}")
    print(f"Сдвиг при округлении к чётному: {shift_even:g}")
    print(f"Разность результатов: {shift_up - shift_even:g}")


def task9():
    terms = [1 / k for k in range(1, 101)]
    exact = math.fsum(terms)
    total = 0.0
    rounded = 0.0
    for x in terms:
        total += x
        rounded += round(x, 3)
    print(f"Эталон: {exact:.16f}")
    for name, value in [("Без округлений", total), ("С округлением", rounded)]:
        print(f"{name}: S = {value:.16f}; ΔS = {absolute_error(value, exact):.6e}; "
              f"δS = {relative_error(value, exact):.6e}")
    error = absolute_error(total, exact)
    if error == 0:
        print("Кратность не определена: без округлений результат совпал с math.fsum.")
    else:
        ratio = absolute_error(rounded, exact) / error
        print(f"Ошибка увеличилась в {ratio:.6e} раз")


def task10():
    result = 0.1 + 0.2
    print("0.1 + 0.2 =", result)
    print("Сравнение через ==:", result == 0.3)
    print("math.isclose:", math.isclose(result, 0.3))
    print(f"Δ = {absolute_error(result, 0.3):.6e}")
    print(f"δ = {relative_error(result, 0.3):.6e}")


def task11():
    result = (1 + 1e-15) - 1
    print(f"a - b = {result:.16e}")
    print(f"δ = {relative_error(result, 1e-15):.6%}")
    a, b, c = 1, 10**8, 1
    d = math.sqrt(b * b - 4 * a * c)
    direct = (-b + d) / (2 * a)
    large_root = (-b - d) / (2 * a)
    stable = c / (a * large_root)
    # Эталон с запасом точности для оценки ошибки малого по модулю корня.
    with localcontext() as ctx:
        ctx.prec = 60
        da, db, dc = Decimal(a), Decimal(b), Decimal(c)
        exact = -2 * dc / (db + (db * db - 4 * da * dc).sqrt())
        direct_error = abs((Decimal.from_float(direct) - exact) / exact)
        stable_error = abs((Decimal.from_float(stable) - exact) / exact)
        print(f"Корень с большим модулем: {large_root:.16e}")
        print(f"Корень с малым модулем (обычно): {direct:.16e}")
        print(f"Корень с малым модулем (устойчиво): {stable:.16e}")
        print(f"Эталон: {exact:.25E}")
        print(f"δ обычной формулы: {direct_error:.6E}")
        print(f"δ устойчивой формулы: {stable_error:.6E}")
        print(f"Уменьшение ошибки: {direct_error / stable_error:.6E} раз")


def task12():
    arr = [0.1] * 1_000_000
    total = 0.0
    for x in arr:
        total += x
    exact = 1e5
    print(f"{'Способ':<12} {'Сумма':>22} {'Δ':>14} {'δ':>14}")
    for name, value in [("Цикл", total), ("sum", sum(arr)), ("math.fsum", math.fsum(arr))]:
        print(f"{name:<12} {value:22.12f} {absolute_error(value, exact):14.6e} "
              f"{relative_error(value, exact):14.6e}")


def task13():
    small = [1e-10] * 500_000
    large = [1e6] * 500_000
    exact = math.fsum(small + large)
    print(f"Эталон: {exact:.10f}")
    for name, arr in [("Маленькие → большие", small + large),
                      ("Большие → маленькие", large + small)]:
        total = 0.0
        for x in arr:
            total += x
        print(f"{name}: {total:.10f}; Δ = {absolute_error(total, exact):.6e}; "
              f"δ = {relative_error(total, exact):.6e}")


def task14():
    x = 1.0
    errors = []
    thresholds = {1e-9: None, 1e-6: None, 1e-3: None}
    for step in range(1, 10_001):
        x *= 1.0001
        exact = math.exp(step * math.log(1.0001))
        error = relative_error(x, exact)
        errors.append(error)
        for threshold in thresholds:
            if thresholds[threshold] is None and error > threshold:
                thresholds[threshold] = step
    print(f"Результат: {x:.16f}")
    print(f"Эталон: {exact:.16f}")
    print(f"Конечная δx: {errors[-1]:.6e}")
    print(f"Максимальная δx: {max(errors):.6e}")
    for threshold, step in thresholds.items():
        print(f"Порог {threshold:g}: {step if step is not None else 'не превышен за 10000 шагов'}")
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, 10_001), errors)
    plt.xlabel("Номер шага")
    plt.ylabel("Относительная погрешность")
    plt.title("Накопление погрешности при умножении на 1.0001")
    plt.grid(True)
    plt.tight_layout()
    path = Path(__file__).with_name("task14_error.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print("График:", path.name)


def task15():
    float_balance = 0.0
    kopecks = 0
    with localcontext() as ctx:
        ctx.prec = 28
        decimal_balance = Decimal("0")
        for _ in range(1_000_000):
            float_balance += 0.01
            decimal_balance += Decimal("0.01")
            kopecks += 1
        difference = abs(Decimal.from_float(float_balance) - decimal_balance)
        print(f"float: {float_balance:.12f} руб.")
        print(f"Decimal: {decimal_balance} руб.")
        print(f"int: {kopecks} коп. = {kopecks // 100}.{kopecks % 100:02d} руб.")
        print(f"Расхождение: {difference:.6E} руб.")
        print(f"Расхождение в процентах: {difference / decimal_balance * 100:.6E}%")


def task16():
    rng = random.Random(42)
    arr = [rng.random() for _ in range(100_000)]
    total = 0.0
    for x in arr:
        total += x
    means = [
        ("Цикл", total / len(arr)),
        ("sum", sum(arr) / len(arr)),
        ("math.fsum", math.fsum(arr) / len(arr)),
        ("numpy.mean", float(np.mean(arr))),
    ]
    epsilon = np.finfo(float).eps
    print(f"ε = {epsilon:.16e}")
    for name, value in means:
        print(f"{name}: {value:.17f}")
    for i in range(len(means)):
        for j in range(i + 1, len(means)):
            name1, value1 = means[i]
            name2, value2 = means[j]
            print(f"{name1} / {name2}: {abs(value1 - value2) / epsilon:g} ε")


def blok1():
    for task in [task1, task2, task3, task4, task5]:
        print(f"\nЗадача {task.__name__[4:]}")
        task()


def blok2():
    for task in [task6, task7, task8, task9]:
        print(f"\nЗадача {task.__name__[4:]}")
        task()


def blok3():
    for task in [task10, task11, task12, task13, task14, task15]:
        print(f"\nЗадача {task.__name__[4:]}")
        task()


if __name__ == "__main__":
    blok1()
    blok2()
    blok3()
    print("\nЗадача 16 (бонус)")
    task16()
