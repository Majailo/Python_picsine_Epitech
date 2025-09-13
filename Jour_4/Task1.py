#Task1.2
"""
i = input("Eris quelque chose !")

if i == "42":
    print("correct")

else :
    print ("non correct")
"""


#Task 1.3
"""
i = input("Ecris un chiffre")

if int(i)%2 == 0:
    print( "paire")
else :
    print("impaire")
"""
#Task 1.4

def acces(x):
    
    if x == "open sesame":
        print("access granted")
    elif x == "will you open, you goddamn !@&/°, display":
        print("access fucking granted")
    else : 
        print("permission denied")

#acces("will you open, you goddamn !@&/°, display")

#Task 1.5

def case1 (x):
    x=int(x)
    if x == 42 :
        print("a")
    elif x/2 <21 :
        print("d")
    elif x <= 21 :
        print("b")
    elif x%2 == 0 :
        print("c")
    elif x%2 != 0 and x>=45 :
        print("e")
    else :
        print("f")

#case1(12)


#Task 1.6

def fix_bug():
    a = 42
    b = 41
    if a == b:
        print ("A and B is the sames ")
    elif b <= a:
        print ("B is equal or lower as A")
    elif b != a:
        print ("B his diferent from A")

fix_bug()