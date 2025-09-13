# task 4.3

meets= [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

#print(*meet)
names=[]
for m in meets:
    names.extend(m[2::])
list(set(names))

name_ip= input(" Donner un nom : ").capitalize()

"""
for name in names:
    for meet in meets:
        if name in meet:
            print(f"{name} à rdv : {meet[0]} à {meet[1]}")
"""

for meet in meets:
    if name_ip in meet:
        print(f"{name_ip} à rdv : {meet[0]} à {meet[1]}")





