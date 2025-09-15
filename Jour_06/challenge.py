# challenge 
import time

start = time.time()

def calcul (exposant) :
    if exposant-1>0:
        result= 42 * calcul(exposant -1)
        return result
    else :
        return 42


print(calcul(84))
print(f" Action réalisé en : {time.time()-start}")