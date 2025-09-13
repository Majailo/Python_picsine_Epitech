# Task 2.1


def r1000():
    for i in range(1, 1001):
        print(i)


# r1000()

# Task 2.2


def twice(x):
    nx = ""
    for elm in x:
        nx += elm * 2
    print(nx)


# twice("Hello")


# Task 2.3


def div7():
    for nb in range(10001, 1, -1):
        if nb % 7 == 0:
            print(nb)


# div7()

# task 2.4


def rd():
    for nb in range(-30, 30):
        if nb % 3 == 0:
            print("Fizz")
        elif nb % 5 == 0 or nb % 3 == 0:
            print("Fizzbuzz")
        elif nb % 5 == 0:
            print("Buzz")
        elif nb % 5 == 0 or nb % 3 == 0:
            print("Fizzbuzz")
        else:
            print(nb)


# rd()


# Task2.5
def dev_beer():
    for nb_beer in range(98, 0, -1):

        print(f"{nb_beer} bottles of beer on the wall.")
        print(f"{nb_beer} bottles of beer.")
        print(f"{nb_beer - 1} bottles of beer.")


# dev_beer()

# task 2.6


def div_a(x):
    nb_div = int(x / 2)
    for nb in range(2, nb_div + 1):
        for z in range(x - 1, 1, -1):
            if z % nb == 0:
                print(z, end=" ")
        print("")


div_a(14)
