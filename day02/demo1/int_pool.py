"""
    小整数池
    范围 -5 ~ 256 这个范围以内的 正数 会自动从小整数池中获取 所以相同取值的变量 指向的是内存中的
    同一个对象 所以地址值相同 使用id()函数可以获取相同的地址值
    使用==比较为True  使用is比较也为True


    在PyCharm中 一个模块文件 直接运行 统一进行编译(.py文件会被编译为.pyc文件)执行的时候 检测到有相同的字面量
    会进行常量折叠：即处理为在内存中使用同一个对象
"""

a = 100
b = 100
c = 100

print(id(a))
print(id(b))
print(id(c))

# ==比较 默认比较值
print(a == b)
print(b == c)


print("-" * 100)
# is比较 比较内存中的地址
print(a is b)
print(a is c)
print(b is c)

print("-" * 100)

d = 300
e = 300
print(d == e) # True

print(d is e) # True

print(id(d) , id(e)) # 相同 1411824327152 1411824327152

