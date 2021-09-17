import hashlib
import random
from math import ceil
from string import ascii_letters, ascii_uppercase, digits

h_str = input("String to hash: ")
n = input("Number of bits to test: ")
h_list = list()
i = 0

n = int(n)

h_start = hashlib.sha1(h_str.encode()).digest()[:ceil(n/8)]
remain = n % 8
h_start = int.from_bytes(h_start) >> remain
#print(h_start)

rando = 'bananas' + str(random.randint(0, 100))

while True:
    rando = rando + str(i)
    h = hashlib.sha1(rando.encode()).digest()[:ceil(n/8)]
    h = int.from_bytes(h) >> remain
    if h == h_start:
        print("Collision at {}".format(i))
        break
    else:
        #print(h)
        #h_list.append(h)
        i += 1

