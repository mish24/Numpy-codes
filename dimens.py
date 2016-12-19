#printing random integers of various dimensions
import numpy as np
print(np.random.randint(1,7))
print(np.random.randint(1, 7, size=1))
print(np.random.randint(1, 7, size=10))
print(np.random.randint(1, 7, size=(10, )))
print(np.random.randint(1, 7, size=(4,5)))
