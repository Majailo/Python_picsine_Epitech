def f1 () :
    return 42

def f2 ( x ):
    return 2 * x

print ( f1 () )
# prediction : 42
print ( f2 (5) + f1 () )
# prediction 10 + 42 = 52