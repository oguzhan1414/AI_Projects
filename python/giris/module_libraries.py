import math
print(math.sqrt(16))

import random ,datetime ,os
print(random.randint(1,10))

import random as rnd

print(rnd.choices(["ayşe","fatma","hayriye"]))

password = "".join(random.choices("abcdefghijklmnsrxyz0123456789",k=10))
print(password)