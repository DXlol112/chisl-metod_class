import math

def absolute_error(exact, measured):
    return abs(exact - measured)

def percentage_error(exact, measured):
    return relative_error(exact, measured) * 100


def relative_error(exact, measured):
    return absolute_error(exact, measured) / abs(exact)

def blok1():

    def task1():
        tasks = [
            ("1. Число π", 3.14, math.pi),
            ("2. Число e", 2.718, math.e),
            ("3. Ускорение g", 9.8, 9.81),
            ("4. Дробь 1/3", 0.333, 1 / 3),
        ]
        for name, approx_x, exact_x in tasks:
            abs_err = absolute_error(exact_x, approx_x)
            perc_err = percentage_error(exact_x, approx_x)

            print(f"{name}:")
            print(f"  Δx = {abs_err:.6f}")
            print(f"  δx = {perc_err:.4f}%\n")

    def task2():
        tasks = [
            ("1. Длина моста", 1247, "м", 1250),
            ("2. Диаметр болта", 9.7, "мм", 10.0),
        ]

        for name, approx_x, unit, exact_x in tasks:
            abs_err = absolute_error(exact_x, approx_x)
            rel_err = relative_error(exact_x, approx_x)

            print(f"{name}:")
            print(f"  Δx = {abs_err:g} {unit}")
            print(f"  δx = {rel_err:g}\n")
    
    def task3():
        

    print("Задача 1. Ручной счёт")
    task1()
    print("Задача 2. Сравнение несопоставимых величин")
    task2()


if __name__ == "__main__":
    blok1()
