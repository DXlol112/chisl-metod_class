import math
from decimal import Decimal, getcontext
import mpmath as mp
import matplotlib.pyplot as plt


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
            print(f"{name:10} | cond = {cond:.4f}")

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
        print(f"{'Эпсилон':<12} {'Сдвиг корня':<16} {'Отношение'}")
        for eplsilon in (1e-2, 1e-4, 1e-6):
            a, b, c = 1.0, -2.0, 1.0 - eplsilon

            D = b**2 - 4 * a * c

            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)

            shift = abs(x1 - 1)

            if previous_shift is None:
                ratio = "-"
            else:
                ratio = f"{previous_shift / shift:.2f}"

            print(f"{eplsilon:<12.0e} {shift:<16.6f} {ratio}")

            previous_shift = shift

    def task4():

        def unstable(x):
            return math.sqrt(x + 1) - math.sqrt(x)

        def stable(x):
            return 1 / (math.sqrt(x + 1) - math.sqrt(x))


        values = [1e2, 1e4, 1e8, 1e12, 1e16, 1e20]

        for x in values:
            a, b = unstable(x), stable(x)
            print(f"x = {x:.0e}\n"
            f"Неустойчивый: {a:.12e}\n"
            f"Устойчивый:   {b:.12e}\n"
            f"Расхождение:  {abs(a - b):.12e}\n"
            )

    task1()
    print()

    task2()
    print()

    task3()
    print()
    
    task4()
    print()

def blok2():
    
    def task5():
        getcontext().prec = 50

        bad = lambda a, b, c: (-b +math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        good = lambda a, b, c: (2 * c) / (-b - math.sqrt(b**2 + 4 * a * c))

        a, c = 1, 1

        print(f"{'b':<10} | {'Ошибка плохого':<20} | {'Ошибка хорошего':<20}")
        for b in (10e4, 10e8, 10e12):
            x_bad = bad(float(a), float(b), float(c))
            x_good = good(float(a), float(b), float(c))

            a_d, b_d, c_d = Decimal(a), Decimal(b), Decimal(c)
            disc_d = (b_d**2 - Decimal(4) * a_d * c_d).sqrt()
            x_exact = (Decimal(2) * c_d) / (-b_d - disc_d)
            err_bad = abs(Decimal(str(x_bad)) - x_exact) / abs(x_exact)
            err_good = abs(Decimal(str(x_good)) - x_exact) / abs(x_exact)

            print(f"{b:<10.0e} | {float(err_bad):<20.3e} | {float(err_good):<20.3e}")
    
    def task6():
        mp.mp.dps = 50

        bad = lambda x: (1 - math.cos(x)) / x**2
        good = lambda x: 2 * math.sin(x / 2)**2 / x**2
        ref = lambda x: (1 - mp.cos(x)) / x**2

        error = lambda value, ref: float(abs(value - ref) / abs(ref))

        nums = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
        bad_errors = []
        good_errors = []

        print(f"{'x':>10} | {'Плохой':>15} | {'Хороший':>15}")

        for num in nums:
            reference = ref(mp.mpf(num))

            bad_error = error(bad(num), reference)
            good_error = error(good(num), reference)

            bad_errors.append(bad_error)
            good_errors.append(good_error)

            print(f"{num:10.0e} | {bad_error:15.6e} | {good_error:15.6e}")

        for num, err in zip(nums, bad_errors):
            if err > 0.01:
                print(f"Ошибка превышает 1% при x = {num:.0e}")
                break

        plt.loglog(nums, bad_errors, "o-", label="Плохой")
        plt.loglog(nums, good_errors, "o-", label="Хороший")

        plt.axhline(0.01, linestyle="--", label="Ошибка 1%")

        plt.xlabel("x")
        plt.ylabel("Относительная ошибка")
        plt.legend()
        plt.grid(True)
        plt.show()

    def task7():
        mp.mp.dps = 50
        bad = lambda x: 1 / (math.sqrt(x + 1) + math.sqrt(x))
        good = lambda x: math.sqrt(x + 1) - math.sqrt(x)
        ref = lambda x: mp.sqrt(x + 1) - mp.sqrt(x)

        error = lambda value, ref: float(abs(value - ref) / abs(ref))

        print(f"{'x':<10} | {'Ошибка плохого':<20} | {'Ошибка хорошего':<20}")
        for num in [1e4, 1e8, 1e12, 1e14, 1e16]:
            reference = ref(mp.mpf(num))

            bad_error = error(bad(num), reference)
            good_error = error(good(num), reference)

            print(f"{num:<10.0e} | {bad_error:<20.6e} | {good_error:<20.6e}")

    def task8():
        bad = lambda x: math.log(1 + x);
        good = lambda x: math.log1p(x)

    task5()
    print()

    task6()
    print()

    task7()
    print()
    

def main():
    blok1()
    blok2()


if __name__ == "__main__":
    main()
