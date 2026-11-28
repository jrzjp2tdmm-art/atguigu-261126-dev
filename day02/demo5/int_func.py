"""
    强制类型转换
"""

print("----------------------int()函数----------------------------")

print(int(1))
print(int(True))
print(int(False))
print(int(3.5)) # 小数位舍弃
print(int("20"),type(int("20")))
print(int("   123    ")) # 会自动去除前后的空白
# print(int("   1 2 3    ")) # ValueError: invalid literal for int() with base 10: '   1 2 3    '
# print(int("abc")) # ValueError: invalid literal for int() with base 10: 'abc'

print(int("111")) # 111
print(int("111",2)) # 7
print(int("11",8)) # 9
print(int("11",16)) # 17
print(int("4E2D",16)) # 20013

print(int("0B111",2))
print(int("0o111",8))
print(int("0x111",16))

# 第二个参数 传入0 表示根据我们字符串的内容 自动进行处理
print(int("0B111",0))
print(int("0o111",0))
print(int("0x111",0))


# print(int("0x111")) # ValueError: invalid literal for int() with base 10: '0x111'









print("程序结束")




