A = 12
B = 18
C = 21
D = 0x0C
E = 0x12

y=(A == B and C != B)
print(y)
y=(not(C == A) or C == B)
print(y)
y=(E == B)
print(y)
y=(A != C)
print(y)
y=(E == B and A != C)
print(y)
y=(E == B or A != C)
print(y)
y=(not(not(E == B) or A == C))
print(y)
y=(A >= B)
print(y)
y=(A <= C)
print(y)
y=(A >= E and C <= D)
print(y)
y=((not(A >= B) or C <= D) and A == C)
print(y)


