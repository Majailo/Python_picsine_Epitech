# la fonction est au final reduite à : f(x) = (2x-1)² /  6 + f(x+1)



def pi_recu(x, lim):
    
    if lim == 0: 
        return 0
    
    if x <= lim :
        return (2*x-1)**2 / (6 + pi_recu(x+1 ,lim))
    else :
        return ((2*x-1)**2) /6 # derniere recurcive 

print(pi_recu(1,700))


