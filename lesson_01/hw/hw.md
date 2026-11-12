# Домашние задания № 1

## Что надо сделать

**17.** Дано число $a = 81{,}359$, определённое с абсолютной погрешностью $\Delta = 0{,}04$. Определить количество верных цифр числа $a$.

**18.** Найдите сумму и разность чисел $x = 35{,}49 \pm 0{,}002$ и $y = 1{,}27 \pm 0{,}003$.

**27.** При численном интегрировании было получено значение определённого интеграла:

$$
a = \int_{1}^{2} \sqrt{x}\,dx \approx 1{,}2188.
$$

Найдите абсолютную и относительную погрешности этого приближения.

## Решение

### Код

```python
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
```

### Вывод

```text
№ 17
Число: 81.359, абсолютная погрешность: 0.04
0.005 < 0.04 ≤ 0.05
Верны 3 значащие цифры (8, 1 и 3), до разряда десятых.

№ 18
Сумма:    36.760 +- 0.005
Разность: 34.220 +- 0.005

№ 27
Значение интеграла по первообразной: 1.218951416497
Абсолютная погрешность: 0.0001514165
Относительная погрешность: 0.0001242186 (0.012422%)

```
