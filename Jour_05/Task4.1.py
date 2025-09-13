# Task 4.1

amba_guests = ["mike", "peter", "john", "carl"]

ac = ["marc", "carl"]

for name in ac:
    if name in amba_guests:
        print(f"Welcome {name}")
    else:
        print(f"you are not on the list Sir __{name}__ !")
