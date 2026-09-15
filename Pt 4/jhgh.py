a = 0x05
b = 0o52
c = 0b01101010
d = 15
print(bin(~a))
print(bin(~b))
print(bin(~c))
print(bin(~d))

print(oct(~a))
print(oct(~b))
print(oct(~c))
print(oct(~d))

print(hex(~a))
print(hex(~b))
print(hex(~c))
print(hex(~d))

print(bin(~(b+c)))
print(oct(~(b+c)))
print(hex(~(b+c)))

print(bin(~(b+~(c))))
print(oct(~(b+~(c))))
print(hex(~(b+~(c))))

print(bin(b+c))
print(oct(b+c))
print(hex(b+c))

print(bin(b+c<<1))
print(oct(b+c<<1))
print(hex(b+c<<1))

print(bin(b+c<<3))
print(oct(b+c<<3))
print(hex(b+c<<3))

print(bin(b+c>>1))
print(oct(b+c>>1))
print(hex(b+c>>1))

print(bin(d|a))
print(oct(d|a))
print(hex(d|a))

print(bin(d&a))
print(oct(d&a))
print(hex(d&a))

print(bin(d^a))
print(oct(d^a))
print(hex(d^a))

print(bin((d|a)|c))
print(oct((d|a)|c))
print(hex((d|a)|c))

print(bin((d&a)&d))
print(oct((d&a)&d))
print(hex((d&a)&d))

print(bin(~(d^a)>>1))
print(oct(~(d^a)>>1))
print(hex(~(d^a)>>1))

print(bin(((((a+(~b))&c^255)*d)<<2)//4))
print(oct(((((a+(~b))&c^255)*d)<<2)//4))
print(hex(((((a+(~b))&c^255)*d)<<2)//4))

