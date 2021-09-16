import hashlib
import random


n = input("Number of bits to test: ")
h_list = list()
i = 0

while True:
    h = hashlib.sha1(bytearray(random.getrandbits(n))).hexdigest()[0:n]
    if h in h_list:
        print("Collision at %d".format(i))
        break
    else:
        h_list.append(h)
        i += 1

