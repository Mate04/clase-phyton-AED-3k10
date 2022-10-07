import numpy as np
import sys
s = range(1000)
print(sys.getsizeof(5)*len(s))
print()
d = np.arange(1000)
print(d.size*d.itemsize)