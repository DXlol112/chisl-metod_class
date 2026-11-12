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
