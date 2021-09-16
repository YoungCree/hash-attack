import hashlib
import random
from string import ascii_letters

h_str = input("String to hash: ")
n = input("Number of bits to test: ")
h_list = list()
i = 0

h_list.append(hashlib.sha1(bytes(h_str.encode())).hexdigest()[0:int(n)])

while True:
    h = hashlib.sha1(bytes(''.join(random.choice(ascii_letters) for j in range(len(h_str))))).hexdigest()[0:int(n)]
    if h in h_list:
        print("Collision at %d".format(i))
        break
    else:
        h_list.append(h)
        i += 1

