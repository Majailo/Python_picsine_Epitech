# challenge

import random
import time

start = time.time()
n = 1000000

# nb = [random.random() for i in range(0, 1000000)]
#nb2 = list(random.sample(range(1, n + 1), n))
nb2 = random.sample(range(n+1), n)
# print(nb)
nb2.sort()
#print(nb2)
# sorted(nb)
# print(nb)
print(f" Action réalisé en : {time.time()-start}")
