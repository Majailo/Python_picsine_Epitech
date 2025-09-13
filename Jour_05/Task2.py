# task 1.9

nb = [1, 2, 3, 4, 5]
result = 1
for elm in nb:
    result *= elm

# print(result)

# print(fruit[::2])


n_l = [x + 10 for x in [3, 2, 6, 7, 1, 4]]
print(n_l)

n_r = list(filter(lambda x: x > 10, [42, 3, 4, 7]))
print(n_r)
