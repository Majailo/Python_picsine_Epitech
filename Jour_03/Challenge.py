# challenge
# recherche de récurence

txt = "the CataCat attaCk a Cat"
txt2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"

patern = ["cat", "garden", "mice"]


def comp_iter(txt, patern_u):

    # mise en forme des entrées

    l_txt = txt.lower()
    s_txt = l_txt.split(" ")
    n_txt = "".join(s_txt)
    rn_txt = n_txt[::-1]
    print(n_txt)
    print(rn_txt)

    nb = 0

    for elm in patern_u:

        patern = elm.lower()
        l_patern = len(patern)

        for i in range(len(rn_txt) + 1):
            ex = n_txt[i : i + l_patern]
            if patern == ex:
                nb += 1

        for i in range(len(rn_txt) + 1):
            ex = rn_txt[i : i + l_patern]
            if patern == ex:
                nb += 1

    print(nb)


comp_iter(txt, patern)
comp_iter(txt2, patern)
