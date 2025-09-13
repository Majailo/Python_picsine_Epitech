# Challenge
def challenge(x):
    ch = []
    st = []
    decompo = []
    vowel = ["a", "e", "i", "o", "u", "y"]
    decompo = x.split()

    for elm in decompo:
        try:
            ch += [int(elm)]
        except:
            st += [elm]

    for nb in ch:
        if nb == 0:
            exit()
        if nb >= 42:
            print(nb)

        for l in st:
            for li in l:
                if li in vowel:
                    print(nb)
                else:
                    print(" ".join(st))


challenge("JAi 32")
