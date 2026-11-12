# Мини-задание для закрепления

## Что надо было сделать

1. Создайте массив формы `(6, 4)` из `np.arange(24)`. Выведите `.shape`, `.ndim`, `.size`, `.dtype`.
2. Перестройте его в `(4, 6)`, затем в `(2, 3, 4)`, затем обратно в `(24,)`. Убедитесь через `np.array_equal`, что значения не изменились.
3. Возьмите столбец `[:, 2]` — это view или копия? Проверьте: измените элемент среза и посмотрите на оригинал.
4. Отфильтруйте элементы `> 10` булевой маской. Посчитайте их среднее.
5. Вычтите из каждой строки её среднее (`axis=1`, keepdims=True) — убедитесь, что результат имеет ту же форму и сумма по строкам ≈ 0.

## Решение

```python
import numpy as np

original = np.arange(24)
matrix = original.reshape(6, 4)

print("1.",
    "\nshape: ", matrix.shape,
    "\nndim: ", matrix.ndim,
    "\nsize:", matrix.size,
    "\ndtype:", matrix.dtype,
    )


print("\n2.")

reshaped = matrix
for shape in ((4, 6), (2, 3, 4), (24,)):
    reshaped = reshaped.reshape(shape)
    print("shape:", reshaped.shape)

print("Значения сохранились:", np.array_equal(original, reshaped))


print("\n3.")

column = matrix[:, 2]
print("Срез разделяет память с исходным массивом:", np.shares_memory(column, matrix))
print("Элемент исходного массива до изменения:", matrix[0, 2])

column[0] = -1
print("Элемент исходного массива после изменения:", matrix[0, 2])


print("\n4.")

mask = matrix > 10
selected = matrix[mask]

print("Элементы:", selected)
print("Среднее:", selected.mean())


print("\n5.")

row_means = matrix.mean(axis=1, keepdims=True)
centered = matrix - row_means
row_sums = centered.sum(axis=1)

print(centered)
print("Форма сохранилась:", centered.shape == matrix.shape)
print("Суммы по строкам:", row_sums)
print("Все суммы близки к нулю:", np.allclose(row_sums, 0))
```

```text
1. 
shape:  (6, 4) 
ndim:  2 
size: 24 
dtype: int64

2.
shape: (4, 6)
shape: (2, 3, 4)
shape: (24,)
Значения сохранились: True

3.
Срез разделяет память с исходным массивом: True
Элемент исходного массива до изменения: 2
Элемент исходного массива после изменения: -1

4.
Элементы: [11 12 13 14 15 16 17 18 19 20 21 22 23]
Среднее: 17.0

5.
[[-0.75  0.25 -1.75  2.25]
 [-1.5  -0.5   0.5   1.5 ]
 [-1.5  -0.5   0.5   1.5 ]
 [-1.5  -0.5   0.5   1.5 ]
 [-1.5  -0.5   0.5   1.5 ]
 [-1.5  -0.5   0.5   1.5 ]]
Форма сохранилась: True
Суммы по строкам: [0. 0. 0. 0. 0. 0.]
Все суммы близки к нулю: True
```