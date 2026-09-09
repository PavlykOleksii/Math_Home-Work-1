import numpy as np

M = np.array([
    [100, 150, 200],
    [50, 100, 150],
    [0, 50, 100]
     ], dtype=float)

E = np.array([
    [20, 30, 40],
    [10, 20, 30],
    [5, 10, 15] 
], dtype=float)

print(M.dtype, " ",M.shape)

contrast = M * 0.5

brightness = M + 25

blend = 0.8*M + 0.2 * E

print("\n",contrast)
print("\n",brightness)
print("\n",blend)