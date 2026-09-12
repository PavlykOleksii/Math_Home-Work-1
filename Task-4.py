import numpy as np

A = np.array([
    [1,1],
    [2,1],
    [3,1],
    [4,1],
    [5,1]
], dtype=float)

y = np.array([22,28,37,45,53], dtype=float)

coefficients = np.linalg.lstsq(A, y, rcond=None)
print(f"\n{coefficients}")

x = coefficients[0]
print("\n", x)

k = x[0]
print(f"\nk = {k:.2f}")
b = x[1]
print(f"b = {b:.2f}")

print(f"Тренд CPU: y = {k:.2f}t + {b:.2f}")

ftime = 6
forecast = k*ftime + b

print(f"Прогнозована завантаженість CPU на {ftime}-й годині буде приблизно {forecast:.2f}%")

AT=A.T
print(A)
print(AT)

print(A.shape)
print(AT.shape)

multATA = AT@A
print(multATA)
print(multATA.shape)

YmiltAT = AT@y
print(YmiltAT)
print(YmiltAT.shape)

kb = np.linalg.solve(multATA,YmiltAT)
print(kb)

if np.allclose(kb,x):
    print("Методи дали однакові коефіцієнти")
else:
    print("Коефіцієнти різні")