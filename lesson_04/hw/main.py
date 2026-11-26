import numpy as np


def block1():

    def task1():
        arr = np.arange(60).reshape(3, 4, 5)
        print(
            f"shape: {arr.shape}\n"
            f"ndim: {arr.ndim}\n"
            f"size: {arr.size}\n"
            f"dtype: {arr.dtype}\n"
            f"strides: {arr.strides}\n"
            f"C_CONTIGUOUS: {arr.flags['C_CONTIGUOUS']}"
            )

    def task2():
        a = np.array([1, 2, 3, 4])
        b = np.array([1, 2, 3], dtype=np.int8)
        b_res = b + 127

        print(
            f"a / 2: {a / 2}\n"
            f"a // 2: {a // 2}\n"
            f"a / 2.0: {a / 2.0}\n"
            f"a.dtype: {a.dtype}\n"
            f"(a / 2).dtype: {(a / 2).dtype}\n"
            f"(a // 2).dtype: {(a // 2).dtype}\n"
            f"b + 127: {b_res}\n"
            f"(b + 127).dtype: {b_res.dtype}"
        )

    def task3():
        err32 = float(np.float32(0.1)) - 0.1
        err64 = float(np.float64(0.1)) - 0.1 # Число 0.1 Уже имеет float64 так что 0
        ratio = abs(err32) / abs(err64) if err64 != 0 else float('inf')

        print(
            f"err32 (repr): {repr(err32)}\n"
            f"err32 (:.20e): {err32:.20e}\n"
            f"err64 (repr): {repr(err64)}\n"
            f"err64 (:.20e): {err64:.20e}\n"
            f"Ошибка float32 больше в {ratio} раз"
            )
        
    def task4():
        a1 = np.zeros((2, 3), dtype=np.float64)
        a2 = np.zeros((2, 3), dtype=np.float32)
        a3 = np.ones((2, 3), dtype=np.int16)
        a4 = np.full((2, 3), 7, dtype=np.uint8)

        big64 = np.zeros((1000, 1000), dtype=np.float64)
        big32 = np.zeros((1000, 1000), dtype=np.float32)

        saved_bytes = big64.nbytes - big32.nbytes

        print(
            f"a1: dtype={a1.dtype}, nbytes={a1.nbytes}\n"
            f"a2: dtype={a2.dtype}, nbytes={a2.nbytes}\n"
            f"a3: dtype={a3.dtype}, nbytes={a3.nbytes}\n"
            f"a4: dtype={a4.dtype}, nbytes={a4.nbytes}\n"
            f"Экономия на (1000, 1000): {saved_bytes} байт ({saved_bytes / 10**6:.2f} МБ)"
        )

    print("Задача 1. Инвентаризация массива")
    task1()
    print()

    print("Задача 2. Целочисленное деление и переполнение")
    task2()
    print()

    print("Задача 3. Точность float32 и float64")
    task3()
    print()

    print("Задача 4. Явный dtype")
    task4()
    print()


def block2():

    def task5():
        a = np.arange(24)
        shapes = [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]

        cur = a

        for s in shapes:
            cur = cur.reshape(s)
            print(f"shape: {cur.shape}, equal: {np.array_equal(a, cur.ravel())}")

    def task6():
        M = np.arange(12).reshape(3, 4)
        f = M.flatten()
        r = M.ravel()

        base_f = f.base is None
        base_r = r.base is not None

        f[0] = 999
        changed_after_f = M[0, 0] == 999

        r[1] = 888
        changed_after_r = M[0, 1] == 888

        print(
            f"f.base is None: {base_f}\n"
            f"r.base is not None: {base_r}\n"
            f"M изменился после f[0] = 999: {changed_after_f}\n"
            f"M изменился после r[1] = 888: {changed_after_r}\n"
            f"Итоговый M:\n{M}"
            )

    def task7():
        v = np.arange(5)
        column = v[:, None]
        row = v[None, :]
        flat = np.squeeze(column)
        transpose = np.arange(6).reshape(2, 3).T
        sums = column + row

        print(f"v[:, None].shape: {column.shape}")
        print(f"v[None, :].shape: {row.shape}")
        print(f"np.squeeze(v[:, None]).shape: {flat.shape}")
        print(f".T {transpose.shape}:\n{transpose}")
        print(f"Таблица сложения {sums.shape}:\n{sums}")

    def task8():
        A = np.arange(6).reshape(2, 3)
        B = A.T
        print(f"B.base is not None: {B.base is not None}")
        print(f"A.strides: {A.strides}, B.strides: {B.strides}")
        B[0, 1] = 999
        print(f"A после изменения B:\n{A}")

    print("Задача 5. Цепочка reshape")
    task5()
    print()

    print("Задача 6. flatten и ravel")
    task6()
    print()

    print("Задача 7. Добавление и удаление осей")
    task7()
    print()

    print("Задача 8. Транспонирование без копии")
    task8()
    print()


def block3():

    def task9():
        A = np.arange(6).reshape(2, 3)
        B = np.arange(6).reshape(3, 2)

        for name, result in (("A @ B", A @ B), ("A.T @ B.T", A.T @ B.T), ("A * A", A * A)):
            print(f"{name}, форма {result.shape}:\n{result}")

        try:
            print(A * B)
        except ValueError as error:
            print(f"A * B: {type(error).__name__}, формы {A.shape} и {B.shape} несовместимы")

        diagonal = np.diag([2, 3])
        print(f"D * D:\n{diagonal * diagonal}")
        print(f"D @ D:\n{diagonal @ diagonal}")

    def task10():
        M = np.arange(12).reshape(3, 4)
        print(f"Суммы столбцов, axis=0: {M.sum(axis=0)}")
        print(f"Суммы строк, axis=1: {M.sum(axis=1)}")
        print(f"Средние столбцов, axis=0: {M.mean(axis=0)}")
        print(f"Средние строк, axis=1: {M.mean(axis=1)}")
        print(f"argmax по столбцам: {M.argmax(axis=0)}")
        print(f"argmax по строкам: {M.argmax(axis=1)}")

        small = np.array([[1, 2], [3, 4]])
        print(f"Маленький пример:\n{small}")
        print(f"По столбцам: {small.sum(axis=0)}, по строкам: {small.sum(axis=1)}")

    def task11():
        X = np.random.default_rng(42).normal(size=(5, 3))

        mean = X.mean(axis=0)
        mean_keep = X.mean(axis=0, keepdims=True)
        centered = X - mean
        centered_keep = X - mean_keep

        print(f"Средние столбцов: {mean}, формы: {mean.shape} и {mean_keep.shape}")
        print(f"Формы после вычитания: {centered.shape} и {centered_keep.shape}")

        std = X.std(axis=1)
        std_keep = X.std(axis=1, keepdims=True)
        normalized = (X - X.mean(axis=1, keepdims=True)) / std_keep
        row_mean = normalized.mean(axis=1)
        row_std = normalized.std(axis=1)

        print(f"std строк: {std}, формы: {std.shape} и {std_keep.shape}")
        print(f"Средние строк близки к 0: {np.allclose(row_mean, 0)}")
        print(f"std строк близки к 1: {np.allclose(row_std, 1)}")

    print("Задача 9. Поэлементное и матричное умножение")
    task9()
    print()

    print("Задача 10. Агрегации по осям")
    task10()
    print()

    print("Задача 11. keepdims и broadcasting")
    task11()
    print()


def block4():

    def task12():
        a = np.arange(10)
        b = a[2:5]
        b[0] = 999
        print(f"a после изменения среза: {a}")

        c = a[2:5].copy()
        c[0] = 111
        print(f"a после изменения копии: {a}")

    def task13():
        a = np.random.default_rng(0).normal(size=20)

        positives = a[a > 0]
        near_zero = a[(a > -1) & (a < 1)]
        print(f"Положительных: {positives.size}")
        print(f"Между -1 и 1: {near_zero.size}")
        print(f"Индексы 0, 5, 10, 15: {a[[0, 5, 10, 15]]}")
        print(f"Выбросы: {a[np.abs(a) > 2]}")

        try:
            print(a[a > 0] & (a < 1))
        except TypeError as error:
            print(f"Выборка и маска: {type(error).__name__}")

        print(f"Значения между 0 и 1: {a[(a > 0) & (a < 1)]}")
        a[a < 0] = 0
        print(f"Отрицательные заменены на 0:\n{a}")

    def task14():
        X = np.random.default_rng(1).normal(size=(100, 3))
        X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
        mean = X_norm.mean(axis=0)
        std = X_norm.std(axis=0)

        print(f"Средние близки к 0: {np.allclose(mean, 0)}")
        print(f"std близки к 1: {np.allclose(std, 1)}")

        D = np.linalg.norm(X_norm[:, None, :] - X_norm[None, :, :], axis=2)
        print(f"Форма D: {D.shape}")
        print(f"Нулевая диагональ: {np.allclose(D.diagonal(), 0)}")
        print(f"Матрица симметрична: {np.allclose(D, D.T)}")

    def task15():
        raw = np.random.default_rng(42).normal(20, 2, (30, 4))
        raw[7, 2] = 100
        print(f"1. shape: {raw.shape}, dtype: {raw.dtype}, size: {raw.size}")

        outliers = np.abs(raw - raw.mean(axis=0)) > 3 * raw.std(axis=0)
        print(f"2. Выбросов: {outliers.sum()}")

        masked = np.where(outliers, np.nan, raw)
        clean = np.where(outliers, np.nanmean(masked, axis=0), masked)
        print(f"3. Замена: {raw[outliers]} → {masked[outliers]} → {clean[outliers]}")

        transposed = clean.T
        back = transposed.T
        print(f"4. .T: {transposed.shape} → {back.shape}, совпало: {np.array_equal(clean, back)}")

        flat = back.ravel()
        data = flat.reshape(raw.shape)
        print(f"5. ravel и reshape: {flat.shape} → {data.shape}, совпало: {np.array_equal(back, data)}")

        mean = data.mean(axis=0)
        std = data.std(axis=0)
        print(f"6. Средние: {mean}\n   std: {std}")

        normalized = (data - mean) / std
        print(f"7. Средние близки к 0: {np.allclose(normalized.mean(axis=0), 0)}")
        print(f"std близки к 1: {np.allclose(normalized.std(axis=0), 1)}")

    print("Задача 12. Срез и копия")
    task12()
    print()

    print("Задача 13. Булева маска и индексы")
    task13()
    print()

    print("Задача 14. Нормировка и расстояния")
    task14()
    print()

    print("Задача 15. Обработка измерений датчиков")
    task15()


def main():
    print("Блок 1. Свойства и типы массивов")
    block1()

    print("Блок 2. Формы и представления массивов")
    block2()

    print("Блок 3. Операции, агрегации и оси")
    block3()

    print("Блок 4. Индексация, выборки и broadcasting")
    block4()


if __name__ == "__main__":
    main()
