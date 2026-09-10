import numpy as np

A = np.array([
    [4, 4, 6],
    [1, 1, 2],
    [1,2,4]
], dtype=float)

b = np.array([460, 130, 240], dtype=float)

dtrmnt = np.linalg.det(A)
print(f"Визначник det(A) = {dtrmnt:.2f}")

if dtrmnt != 0:
    print("Є єдиний розв'язок")
else:
    print("Єдиного розв'язку немає")

x = np.linalg.solve(A,b)
print("Кількість дронів Розвідник:", x[0])
print("Кількість дронів Камікадзе:", x[1])
print("Кількість дронів Вантажний:", x[2])

checkb = A @ x

if np.allclose(checkb, b):
    print("Задача розв'язана вірно")
else:
    print("Не вірний розв'язок")