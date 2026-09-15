a = 0x15
b = 0o25
c = 0b00101110
d = 52

import math
y=math.ceil((a^b)*d)
print(y)

import math
y=math.floor(math.fabs(a/d)*c)
print(y)

import math
y=math.ceil((math.tan(a)/b)*c)
print(y)

import math
y=math.floor((a^c)*d)
print(y)

import math
y=math.floor((a^(math.factorial(5)))*math.log(15))
print(y)

import math
y=math.ceil((a^(math.factorial(5)))*math.log(15)*math.pi)
print(y)

import math
y=math.floor(math.cos((a^c)*d))
print(y)
