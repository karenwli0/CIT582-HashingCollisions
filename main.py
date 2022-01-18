import hashlib

# word = "Bitcoin"
# a = hashlib.sha256(word.encode('utf-8')).hexdigest()
# print(a)
from hash_collision import hash_collision

string = "Bitcoin"
m = hashlib.sha256()
for c in string:
    m.update(c.encode('utf-8'))
    print(m.hexdigest())

print(bin(int(m.hexdigest(), base= 16)))

import string
import random
print(random.choice(string.ascii_letters))

print(hash_collision(4))

a = 'f'
print(hashlib.sha256(a.encode('utf-8')).hexdigest())
b = 'gfJEzYZDf'
print(hashlib.sha256(b.encode('utf-8')).hexdigest())
