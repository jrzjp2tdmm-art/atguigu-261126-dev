"""
    每个（字符串），不夹杂空格或者特殊符号，
    默认开启intern机制，共享内存，
    靠引用计数决定是否销毁。
    相同的字符串默认只保留一份，当创建一个字符串，
    它会先检查内存里有没有这个字符串，如果有就不再创建新的了。

    单个字母，长度为1的 ASCII(美国标准信息交换码) 字符会被 interned，包括空字符。
"""

s1 = "abc"
s2 = "abc"
s3 = "abc"

print(id(s1), id(s2), id(s3))
print(s1 is s2)
print(s2 is s3)

print("*" * 100)

str1 = "a b c"
str2 = "a b c"
print(str1 is str2)


print("*" * 100)


c1 = 'a'
c2 = 'a'
print(c1 is c2)

c3 = ' '
c4 = ' '
print(c3 is c4)


