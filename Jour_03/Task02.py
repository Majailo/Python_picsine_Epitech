#Task 2.2

txt = "tu as besoin de tu"

print(txt.replace("tu","ta"))


"""
compt=0
for elm in txt:
    compt+=1
    if elm == "t" and txt[compt]:
        txt[compt]="a"
    
print(txt)
"""

#Task 2.3

string = " Hello world !"
position = string.find ("a")
print ( position )


#Task 2.4

p = "abcdefghij "
print (p [:: -2][:5][::-1][3:])


#Task 2.5
q=p[:: -2]
r=q[:5]
s=r[::-1]
t=s[3:]
#print (t)

print(p[::-1][3:5])


#Task 2.6
"""
print(txt*10)

for i in range (11):
    print (txt)
"""

#Task 2.7

print("hello" + str(42))


#Task 2.8

s1, s2, s3 = "42" , "is", "the answer"

print(s1+" "+ s2 + " " + s3)
print(f"{s1} {s2} {s3}")

