# Task 3.4

dogs = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 3 * 2 * 111,
    "life": 42,
    "googol": 10**100,
}

v = max(dogs.values())  # cherche la valeur max dans le dico dogs

for key in dogs:
    if dogs.get(key) == v:
        print(key)


"""
for key, value in dogs:
    print(key)
    print(value)
"""
