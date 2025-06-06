import numpy as np

x = 5

for i in range(5):
    x = (np.sqrt( x*x*x/-6 + 19*x/6 + 14))
    print (np.round(x,2), "->", x)