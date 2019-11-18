import numpy as np
X = np.random.random((5,5))
x = np.mean(X)
sd=np.std(X)
Z = (X-x)/sd
print(Z)
