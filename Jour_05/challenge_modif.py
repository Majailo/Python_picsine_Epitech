import time
import random

start = time.time()
n = 1000000
my_list = list(random.sample(range(1, n + 1), n))
sorted_list = my_list.sort()

print(my_list)
print(time.time() - start)
