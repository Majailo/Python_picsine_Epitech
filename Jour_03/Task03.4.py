# task 3.4

#txt = input("ecrivez un text : ")

txt = "Play your trumpet happily on nights."
list_txt=txt.split()
n_word=[]
for elm in list_txt:
    n_word+= elm[0]

print("".join(n_word))


