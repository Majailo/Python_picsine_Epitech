def integer(number):
    print(int(number))



#integer(25.665453)


def decimal(number):
    print(format(number%1,"g"))
    

decimal(54432.6543)


def decimal2(number):
    number=number-int(number)
    print(format(number, 'g'))


decimal2(4343.55543)
