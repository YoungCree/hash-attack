import hashlib
import random
from string import ascii_letters, ascii_uppercase, digits

h_str = input("String to hash: ")
n = input("Number of bits to test: ")
h_list = list()
i = 0

h_list.append(hashlib.sha1(bytes(h_str.encode())).digest()[0:int(n)])

while True:
    h = hashlib.sha1(bytes(''.join(random.choices(ascii_letters + digits, k=len(h_str))).encode())).digest()[0:int(n)]
    if h == h_list[0]:
        print("Collision at {}".format(i))
        break
    else:
        #h_list.append(h)
        i += 1

