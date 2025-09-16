# Pendu
import random
from english_words import get_english_words_set

import datetime
import time

start = time.time()
time.sleep(1)
rm=""
#english_words
#print (random.shuffle(english_word)
web2lowerset = get_english_words_set(['web2'],lower=True)
#l_web2=list(web2lowerset)

while len(rm) != 6:
    rm=random.choice(list(web2lowerset))
#print(rm)

delta = time.time() -start
#datetime.timedelta(datetime.datetime.now(),)
print(type(delta))
