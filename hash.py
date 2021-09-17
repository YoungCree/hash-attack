import hashlib
import random
from string import ascii_letters, ascii_uppercase, digits

h_str = input("String to hash: ")
n = input("Number of bits to test: ")
h_list = list()
i = 0

h_start = hashlib.sha1(h_str.encode()).digest()[0:int(n)]
#print(h_start)

rando = ''.join(random.choices(ascii_letters + digits, k=len(h_str))).encode()

while True:
    rando = rando + bytes(i)
    h = hashlib.sha1(rando).digest()[0:int(n)]
    if h == h_start:
        print("Collision at {}".format(i))
        break
    else:
        #print(h)
        #h_list.append(h)
        i += 1

