"""
str()函数 将指定的对象转换为字符串
repr()函数 将对象x转换为一个字符串，可以转义字符串中的特殊字符
"""

print(str(100))
print(str(1.2))
print(str(True))
print(str(False))
print(str(None))
print(str("a\nb"))

age = 18
print("我的年龄是" + str(age))

print("----------------------------------------------")

print(repr(100))
print(repr(1.2))
print(repr(True))
print(repr(False))
print(repr(None))
print(repr("a\nb"))
