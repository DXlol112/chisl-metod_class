import math

def blok1():

    def task1():

        def absolute_error(exact, measured):
            return abs(exact - measured)

        def percentage_error(exact, measured):
            return (absolute_error(exact,measured) / measured) * 100

        tasks = [
                ("1. Число Пи", 3.14, math.pi),
                ("2. Число e", 2.718, math.e),
                ("3. Ускорение g", 9.8, 9.81),
                ("4. Дробь 1/3", 0.333, 1 / 3)
            ]
        for name, approx_x, exact_x in tasks:
            abs_err = absolute_error(exact_x, approx_x)
            perc_err = percentage_error(exact_x, approx_x)
            
            print(f"{name}:")
            print(f"  Δx = {abs_err:.6f}")
            print(f"  δx = {perc_err:.4f}%\n")


