from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
x = "01110100 01100101 00100000 01100001 01101101 01101111 00100000 01101101 01100001 01110010 01110100 01101001 00100000 00111100 00110011."
letra = ''
palabra = ''
for i in x:
    if i in " .":
        palabra += decode_binary_string(letra)
        letra = ''
    else:
        letra += i
print(palabra)
