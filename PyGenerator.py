import numpy as np
import time

start_time = time.time()
count = 100000
gen_file = open('py_out.csv', 'w')

while count > 0:
    buff = np.random.randint(10, 99, 1000)
    gen_file.write(str(buff))
    count -= 1

gen_file.write(str(time.time() - start_time) + "sec")
print(time.time() - start_time)
gen_file.close()

