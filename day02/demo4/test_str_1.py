"""
    str类型 字符串类型  Python中没有字符类型 不同于Java 存在char类型
"""

s1 = "hello   '666666' world"
print(s1)
s2 = 'hello   "666666" world'
print(s2)

s3 = """
    床前明月光，
    疑是地上霜。
    ……
"""
print(s3)

s4 = ' 床前明月光，\
    疑是地上霜。'

print(s4)

s5 = '\\'
print(s5)

s6 = '\\\\'
print(s6)

s7 = '\''
print(s7)

s7 = "'"
print(s7)


s8 = "\""
print(s8)

s9 = '"'
print(s9)


s10 = "abc\b"
print(s10)

s1 = "ab\bc"
print(s1)

print("abc\nd\ne\nf")


# \t 制表符 在字符串中间间隔相同的空白
print("床\t\t前\t明\t月\t光")
print("疑\t\t是\t地\t上\t霜")

# \r 回车  回车的本意不是换行 是回到行首 称之为回车

s11 = "abc\rdef"
print(s11)

# 在PyCharm中 遇到\r 是将前边的内容全部删除 重新创建新的字符串对象
s12 = "abcd\refg"
print(s12)








