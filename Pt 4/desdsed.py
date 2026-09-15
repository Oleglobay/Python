A = 0x05
B = 0o52
C = 0b01101010
D = 152

import math
Y = math.ceil ((A & (math.factorial(5))) >> math.ceil(math.log(15)) * math.floor(~C))
print(Y)

import math
Y = math.ceil ((A | (math.factorial(5))) << math.ceil(math.log(15)) * math.floor(~C))
print(Y)


import math
Y = math.ceil (~((A | (math.factorial(5))) >> math.ceil(math.log(15))))
print(Y)
