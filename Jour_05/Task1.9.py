# task 1.9

fruit = ["banane", "pomme", " fraise", "orange", "citron"]


# print(fruit[::2])


# Task 1.10

for i in range(11, 22):
    fruit.append(i)

print(fruit)


# Task 1.11

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]

print(my_first_list)
