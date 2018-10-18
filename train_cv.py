import numpy as np
import time
from collections import Counter

start_time = time.time()

buff = np.random.randint(1, 99, 100000000)

print("Random list", len(buff), "of elements - GENERATED")
print("--- %s seconds ---" % (time.time() - start_time))
print(Counter(buff))
print("--- %s seconds ---" % (time.time() - start_time))
