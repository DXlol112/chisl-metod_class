import math
import random
from array import array
from decimal import Decimal, getcontext

import mpmath as mp
import matplotlib.pyplot as plt
import numpy as np


def relative_error(value, reference):
    return float(abs(value - reference) / abs(reference))


def naive_sum(values):
    total = 0.0
    for value in values:
        total += value
    return total


def sqrt_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)


def sqrt_good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))


def sqrt_ref(x):
    return mp.sqrt(x + 1) - mp.sqrt(x)


def log_bad(x):
    return math.log(1 + x)


def blok1():

    def task1():
        tasks = [
            ("1. sqrt(x)", lambda x: math.sqrt(x), lambda x: 1 / (2 * math.sqrt(x)), 1e-8),
            ("2. ln(x)", lambda x: math.log(x), lambda x: 1 / x, 1.001),
            ("3. x - 1", lambda x: x - 1, lambda x: 1, 1.000001),
            ("4. sin(x)", lambda x: math.sin(x), lambda x: math.cos(x), math.pi / 2),
        ]

        for name, f, df, x in tasks:
            cond = abs(x * df(x) / f(x))
            condition = "хорошо обусловлена" if cond <= 1 else "плохо обусловлена"
            print(f"{name:10} | cond = {cond:.4f} | {condition}")

    def task2():
        a = 1 + 1e-8
        b = 1.0
        delta_a = 1e-9
        f = a - b
        perturbed_f = (a + delta_a) - b
        delta_f = perturbed_f - f

        cond_a = abs(a / f)
        cond_b = abs(b / f)
        relative_delta_a = abs(delta_a / a)
        relative_delta_f = abs(delta_f / f)
        predicted_relative_delta_f = cond_a * relative_delta_a
        observed_cond_a = relative_delta_f / relative_delta_a

        print("cond_a = |a| / |a − b|, cond_b = |b| / |a − b|")
        print(f"cond_a = {cond_a:.8e}, cond_b = {cond_b:.8e}")
        print(f"f(a, b) = {f:.8e}, f(a + δa, b) = {perturbed_f:.8e}")
        print(f"Относительное изменение a = {relative_delta_a:.8e}")
        print(f"{'Величина':<29} | {'Факт':>14} | {'Прогноз':>14}")
        print(f"{'Δf':<29} | {delta_f:14.8e} | {delta_a:14.8e}")
        print(f"{'Δf / δa':<29} | {delta_f / delta_a:14.8e} | {1:14.8e}")
        print(f"{'|Δf / f|':<29} | {relative_delta_f:14.8e} | {predicted_relative_delta_f:14.8e}")
        print(f"{'|Δf / f| / |δa / a|':<29} | {observed_cond_a:14.8e} | {cond_a:14.8e}")

    def task3():
        previous_shift = None
        print(f"{'Эпсилон':<12} {'x1':<12} {'x2':<12} {'Сдвиг корня':<16} {'Отношение'}")
        for epsilon in (1e-2, 1e-4, 1e-6):
            a, b, c = 1.0, -2.0, 1.0 - epsilon

            D = b**2 - 4 * a * c

            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)

            shift = abs(x1 - 1)

            if previous_shift is None:
                ratio = "-"
            else:
                ratio = f"{previous_shift / shift:.2f}"

            print(f"{epsilon:<12.0e} {x1:<12.6f} {x2:<12.6f} {shift:<16.6f} {ratio}")

            previous_shift = shift

    def task4():
        def unstable(x):
            return 1 - 1 / (1 + x)

        def stable(x):
            return x / (1 + x)

        print("f(x) = 1 − 1 / (1 + x) = x / (1 + x), cond = 1 / (1 + x)")
        values = [1e-2, 1e-4, 1e-8, 1e-12, 1e-16, 1e-20]
        print(f"{'x':<10} | {'cond':>12} | {'Неустойчивый':>18} | {'Устойчивый':>18} | {'Расхождение':>18}")
        for x in values:
            a, b = unstable(x), stable(x)
            cond = 1 / (1 + x)
            print(f"{x:<10.0e} | {cond:12.8f} | {a:18.12e} | {b:18.12e} | {abs(a - b):18.12e}")

    print("Задача 1. Число обусловленности")
    task1()
    print()

    print("Задача 2. Вычитание близких чисел")
    task2()
    print()

    print("Задача 3. Обусловленность кратного корня")
    task3()
    print()

    print("Задача 4. Обусловленность и устойчивость")
    task4()
    print()


def blok2():

    def task5():
        getcontext().prec = 50

        bad = lambda a, b, c: (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        good = lambda a, b, c: (2 * c) / (-b - math.sqrt(b**2 - 4 * a * c))

        a, c = 1, 1

        print(f"{'b':<10} | {'Ошибка плохого':<20} | {'Ошибка хорошего':<20}")
        for b in (10**4, 10**8, 10**12):
            x_bad = bad(float(a), float(b), float(c))
            x_good = good(float(a), float(b), float(c))

            a_d, b_d, c_d = Decimal(a), Decimal(b), Decimal(c)
            disc_d = (b_d**2 - Decimal(4) * a_d * c_d).sqrt()
            x_exact = (Decimal(2) * c_d) / (-b_d - disc_d)
            err_bad = relative_error(Decimal.from_float(x_bad), x_exact)
            err_good = relative_error(Decimal.from_float(x_good), x_exact)

            print(f"{b:<10.0e} | {err_bad:<20.3e} | {err_good:<20.3e}")

    def task6():
        mp.mp.dps = 50

        bad = lambda x: (1 - math.cos(x)) / x**2
        good = lambda x: 2 * math.sin(x / 2)**2 / x**2
        ref = lambda x: (1 - mp.cos(x)) / x**2

        nums = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
        bad_errors = []
        good_errors = []

        print(f"{'x':>10} | {'Плохой':>15} | {'Хороший':>15}")
        for num in nums:
            reference = ref(mp.mpf(num))
            bad_error = relative_error(bad(num), reference)
            good_error = relative_error(good(num), reference)
            bad_errors.append(bad_error)
            good_errors.append(good_error)
            print(f"{num:10.0e} | {bad_error:15.6e} | {good_error:15.6e}")

        for num, err in zip(nums, bad_errors):
            if err > 0.01:
                print(f"Ошибка превышает 1% при x = {num:.0e}")
                break

        plt.figure("Задача 6. Косинус при малых x")
        plt.loglog(nums, bad_errors, "o-", label="Плохой")
        plt.loglog(nums, good_errors, "o-", label="Хороший")
        plt.axhline(0.01, linestyle="--", label="Ошибка 1%")
        plt.xlabel("x")
        plt.ylabel("Относительная ошибка")
        plt.legend()
        plt.grid(True, which="both")
        plt.tight_layout()

    def task7():
        mp.mp.dps = 50
        nums = [1e4, 1e8, 1e12, 1e14, 1e16]
        bad_errors = []

        print(f"{'x':<10} | {'Ошибка плохого':<20} | {'Ошибка хорошего':<20}")
        for num in nums:
            reference = sqrt_ref(mp.mpf(num))
            bad_error = relative_error(sqrt_bad(num), reference)
            good_error = relative_error(sqrt_good(num), reference)
            bad_errors.append(bad_error)
            print(f"{num:<10.0e} | {bad_error:<20.6e} | {good_error:<20.6e}")

        slope = np.polyfit(np.log10(nums[:-1]), np.log10(bad_errors[:-1]), 1)[0]
        print(f"Показатель степени на [1e4, 1e14] = {slope:.3f}")

    def task8():
        mp.mp.dps = 50
        print(f"{'x':<10} | {'Ошибка плохого':<20} | {'Ошибка хорошего':<20}")
        for num in [1e-2, 1e-8, 1e-12, 1e-16]:
            reference = mp.log(1 + mp.mpf(num))
            bad_error = relative_error(log_bad(num), reference)
            good_error = relative_error(math.log1p(num), reference)
            print(f"{num:<10.0e} | {bad_error:<20.6e} | {good_error:<20.6e}")

    def task9():
        mp.mp.dps = 50
        nums = [10**5, 10**6, 10**7]
        naive_errors = []
        sum_errors = []
        fsum_errors = []

        print(f"{'n':>10} | {'Ошибка цикла':>15} | {'Ошибка sum':>15} | {'Ошибка fsum':>15}")
        for n in nums:
            arr = array("d", (1 / k for k in range(1, n + 1)))
            reference = mp.harmonic(n)
            naive_error = relative_error(naive_sum(arr), reference)
            sum_error = relative_error(sum(arr), reference)
            fsum_error = relative_error(math.fsum(arr), reference)
            naive_errors.append(naive_error)
            sum_errors.append(sum_error)
            fsum_errors.append(fsum_error)
            print(f"{n:10d} | {naive_error:15.6e} | {sum_error:15.6e} | {fsum_error:15.6e}")

        slope = np.polyfit(np.log10(nums), np.log10(naive_errors), 1)[0]
        print(f"Показатель степени для цикла = {slope:.3f}")
        above_limit = [n for n, error in zip(nums, naive_errors) if error > 1e-10]
        print(f"n с ошибкой цикла > 1e-10: {above_limit}")

        plt.figure("Задача 9. Гармоническая сумма")
        plt.loglog(nums, naive_errors, "o-", label="Цикл")
        plt.loglog(nums, sum_errors, "s--", label="sum")
        plt.loglog(nums, fsum_errors, "x:", label="math.fsum")
        plt.xlabel("n")
        plt.ylabel("Относительная ошибка")
        plt.legend()
        plt.grid(True, which="both")
        plt.tight_layout()

    print("Задача 5. Квадратное уравнение")
    task5()
    print()

    print("Задача 6. Косинус при малых x")
    task6()
    print()

    print("Задача 7. Разность корней при больших x")
    task7()
    print()

    print("Задача 8. Логарифм при малых x")
    task8()
    print()

    print("Задача 9. Накопление ошибки в сумме")
    task9()
    print()


def blok3():

    def task10():
        mp.mp.dps = 50

        def bad(x):
            one = type(x)(1)
            return (one - np.cos(x)) / (x * x)

        def good(x):
            two = type(x)(2)
            sine = np.sin(x / two)
            return two * sine * sine / (x * x)

        def error(f, x):
            x_mp = mp.mpf(float(x))
            reference = (1 - mp.cos(x_mp)) / x_mp**2
            return relative_error(float(f(x)), reference)

        x64 = np.float64(1e-4)
        experiments = [
            ("x: 1e-2 → 1e-4", error(bad, np.float64(1e-2)), error(bad, x64)),
            ("float64 → float32", error(bad, x64), error(bad, np.float32(x64))),
            ("Плохой → хороший", error(bad, x64), error(good, x64)),
        ]

        print(f"{'Фактор':<20} | {'Ошибка до':>14} | {'Ошибка после':>14} | {'log10(после / до)':>18}")
        for name, before, after in experiments:
            orders = math.log10(after / before)
            print(f"{name:<20} | {before:14.6e} | {after:14.6e} | {orders:+18.3f}")

    def task11():
        mp.mp.dps = 50
        x = 1e16
        a = sqrt_bad(x)
        b = math.sqrt(x) * (math.sqrt(1 + 1 / x) - 1)
        reference = sqrt_ref(mp.mpf(x))

        print(f"x = {x:.0e}, a == b: {a == b}, эталон = {mp.nstr(reference, 20)}")
        print(f"{'Алгоритм':<33} | {'Результат':>14} | {'Ошибка':>14}")
        print(f"{'sqrt(x + 1) − sqrt(x)':<33} | {a:14.6e} | {relative_error(a, reference):14.6e}")
        print(f"{'sqrt(x) · (sqrt(1 + 1/x) − 1)':<33} | {b:14.6e} | {relative_error(b, reference):14.6e}")

    def task12():
        mp.mp.dps = 50
        nums = np.logspace(2, 16, 15)
        bad_errors = []
        good_errors = []

        for num in nums:
            reference = sqrt_ref(mp.mpf(float(num)))
            bad_errors.append(relative_error(sqrt_bad(num), reference))
            good_errors.append(relative_error(sqrt_good(num), reference))

        slope = np.polyfit(np.log10(nums[:-2]), np.log10(bad_errors[:-2]), 1)[0]
        print(f"Наклон на [1e2, 1e14] = {slope:.3f}, теоретический наклон = 1")

        plt.figure("Задача 12. Разность корней на диапазоне x")
        plt.loglog(nums, bad_errors, "o-", label="Плохой")
        plt.loglog(nums, good_errors, "o-", label="Хороший")
        plt.loglog(nums, np.finfo(float).eps * nums, "--", label="εmachine · x")
        plt.xlabel("x")
        plt.ylabel("Относительная ошибка")
        plt.legend()
        plt.grid(True, which="both")
        plt.tight_layout()

    def task13():
        def experiment(seed):
            random.seed(seed)
            rng = np.random.default_rng(seed)
            return {
                "random": [random.uniform(-1, 1) for _ in range(10**5)],
                "default_rng": rng.uniform(-1, 1, 10**5).tolist(),
            }

        print(f"n = {10**5}")
        print(
            f"{'seed':>4} | {'Генератор':<12} | {'Запуск':>6} | "
            f"{'sum':>22} | {'math.fsum':>22} | {'numpy.sum':>22} | "
            f"{'sum − fsum':>12} | {'numpy − fsum':>12}"
        )
        for seed, run in [(42, 1), (42, 2), (43, 1)]:
            for name, values in experiment(seed).items():
                total = sum(values)
                precise = math.fsum(values)
                numpy_total = np.sum(values)
                print(
                    f"{seed:4d} | {name:<12} | {run:6d} | "
                    f"{total:22.17g} | {precise:22.17g} | {numpy_total:22.17g} | "
                    f"{total - precise:12.3e} | {numpy_total - precise:12.3e}"
                )

    def task14():
        finite = [1e300, 1e-300, 0.0, 1e-320, -1e300]
        cases = [
            ("Большие", [1e300, 1e300]),
            ("Малые", [1e-300, 1e-300]),
            ("Ноль", [0.0]),
            ("Денормализованные", [1e-320, 1e-320]),
            ("Смесь конечных", finite),
            ("Смесь с inf", finite + [math.inf]),
            ("Смесь с -inf", finite + [-math.inf]),
            ("Смесь с nan", finite[:2] + [math.nan] + finite[2:]),
            ("Смесь с inf и nan", finite + [math.inf, math.nan]),
            ("Смесь с inf и -inf", finite + [math.inf, -math.inf]),
        ]

        print(f"{'Набор':<22} | {'Цикл':>15} | {'math.fsum':>15}")
        for name, values in cases:
            try:
                precise = f"{math.fsum(values):.6e}"
            except ValueError as error:
                precise = type(error).__name__
            print(f"{name:<22} | {naive_sum(values):15.6e} | {precise:>15}")

    def task15():
        mp.mp.dps = 50
        nums = np.logspace(-16, -2, 15)

        print("f(x) = ln(1 + x), эталон mpmath с 50 знаками")
        print(
            f"{'x':>10} | {'Плохой':>21} | {'Хороший':>21} | {'Эталон':>21} | "
            f"{'Ошибка плохого':>15} | {'Ошибка хорошего':>15}"
        )
        for num in nums:
            x = float(num)
            bad = log_bad(x)
            good = math.log1p(x)
            reference = mp.log(1 + mp.mpf(x))
            bad_error = relative_error(bad, reference)
            good_error = relative_error(good, reference)
            print(
                f"{x:10.0e} | {bad:21.14e} | {good:21.14e} | {mp.nstr(reference, 15):>21} | "
                f"{bad_error:15.6e} | {good_error:15.6e}"
            )

    print("Задача 10. Разделение источников ошибки")
    task10()
    print()

    print("Задача 11. Сравнение с эталоном")
    task11()
    print()

    print("Задача 12. Диапазон входных значений")
    task12()
    print()

    print("Задача 13. Воспроизводимость эксперимента")
    task13()
    print()

    print("Задача 14. Границы представимости")
    task14()
    print()

    print("Задача 15. Полный эксперимент для логарифма")
    task15()
    print()


def main():
    print("Блок 1. Обусловленность задачи")
    blok1()

    print("Блок 2. Устойчивость алгоритма")
    blok2()

    print("Блок 3. Корректная постановка эксперимента")
    blok3()

    plt.show()


if __name__ == "__main__":
    main()
