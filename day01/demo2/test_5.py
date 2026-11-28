"""
    变量的修改
    变量：variable 可以随意改变的数据

"""

s1 = "abc"
s2 = "def"
print(s1 + s2)  # 字符串与字符串相加 属于拼接操作 可以正常使用

a = 100
print("a变量的取值为：", a)
a = 200
# print("a变量修改之后的取值为：" + a) # 这里报错 因为str 不能和 int类型相加
print(f"a变量修改之后的取值为：{a}")

s3 = "abc"
s3 = "hello"
print(s3)

print("*" * 50)  # 字符串乘法计算 即赋值对应的次数

print("abc" * 3)

v1 = 10
v2 = 20
print("v1:", v1, "v2:", v2)

v1, v2 = v2, v1  # 交换数据 Python特有的语法糖 直接一语句搞定
print("v1:", v1, "v2:", v2)

print("*" * 50)
# Java中必须按以下方式书写 比较啰嗦
a = 100
b = 200
temp = a
a = b
b = temp
