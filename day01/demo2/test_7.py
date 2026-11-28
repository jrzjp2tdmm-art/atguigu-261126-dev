"""
    各种进制整数的赋值方式
"""

# 二进制 0b 或者 0B开头

a = 0B11
print(a)

b = 0O11
print(b)

c = 100
print(c)

d = 0X11
print(d)

e = 0X4E2D # 20013
print(e)

f = 0X4E00 # 19968 中文汉字 一
print(f)

g = 0X9FA5 # 40869 中文汉字
print(g)

print("*" * 50)

a1 = 3
print(bin(a1)) # bin binary 二进制 转换为二进制

a2 = 9
print(oct(a2))

a3 = 17
print(hex(a3))


