from math import sqrt


def task_17():
    value = 81.359
    absolute_error = 0.04
    half_tenth = 0.1 / 2
    half_hundredth = 0.01 / 2

    print("№ 17")
    print(f"Число: {value:g}, абсолютная погрешность: {absolute_error:g}")
    
    if half_hundredth < absolute_error <= half_tenth:
        print(f"{half_hundredth:g} < {absolute_error:g} ≤ {half_tenth:g}")
        print("Верны 3 значащие цифры (8, 1 и 3), до разряда десятых.")


def task_18():
    x, x_error = 35.49, 0.002
    y, y_error = 1.27, 0.003
    result_error = x_error + y_error

    print("\n№ 18")
    print(f"Сумма:    {x + y:.3f} +- {result_error:.3f}")
    print(f"Разность: {x - y:.3f} +- {result_error:.3f}")


def task_27():
    approximation = 1.2188
    lower, upper = 1, 2
    exact_value = (2 / 3) * (upper * sqrt(upper) - lower * sqrt(lower))
    absolute_error = abs(exact_value - approximation)
    relative_error = absolute_error / abs(exact_value)

    print("\n№ 27")
    print(f"Значение интеграла по первообразной: {exact_value:.12f}")
    print(f"Абсолютная погрешность: {absolute_error:.10f}")
    print(f"Относительная погрешность: {relative_error:.10f} ({relative_error:.6%})")


if __name__ == "__main__":
    task_17()
    task_18()
    task_27()
