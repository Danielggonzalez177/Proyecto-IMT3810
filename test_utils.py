import numpy as np

from utils import E, Q

x = np.random.rand(3)
y = np.random.rand(3)

print(f"E(x,y) = \n{E(x, y)}\n")
print(f"Q(x,y) = \n{Q(x, y)}")
