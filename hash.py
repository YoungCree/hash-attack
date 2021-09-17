import hashlib
import random
from math import ceil
from string import ascii_letters, ascii_uppercase, digits

h_str = input("String to hash: ")
n = input("Number of bits to test: ")
is_collision = input("Perform collision or pre-image attack? (c/p): ")
h_list = list()
i = 0

n = int(n)

h_start = hashlib.sha1(h_str.encode()).digest()[:ceil(n/8)]
remain = 8 - (n % 8)
h_start = int.from_bytes(h_start, byteorder='big') >> remain
#print(h_start)

rando = 'bananas' + str(random.randint(0, 100))


if (is_collision == 'c'):
    while True:
        rando = rando + str(i)
        h = hashlib.sha1(rando.encode()).digest()[:ceil(n/8)]
        h = int.from_bytes(h, byteorder='big') >> remain
        if h == h_start:
            print("Collision at {}".format(i))
            break
        else:
            #print(h)
            #h_list.append(h)
            i += 1
else:
    h_list.append(h_start)
    while True:
        rando = rando + str(i)
        h = hashlib.sha1(rando.encode()).digest()[:ceil(n/8)]
        h = int.from_bytes(h, byteorder='big') >> remain
        if h in h_list:
            print("Collision at {}".format(i))
            break
        else:
            #print(h)
            h_list.append(h)
            i += 1

