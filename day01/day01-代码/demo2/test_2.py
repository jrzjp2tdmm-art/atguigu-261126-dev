"""
    Python中的变量定义
"""


# 方式1  直接使用=号赋值变量
a = 100 # int类型 Integer 表示整数类型
b = "hello world" #str  string类型 表示字符串
c = True # bool  boolean 布尔类型


# 方式2
# 多个变量使用相同的值
a1 = a2 = a3 = 200
print(a1,a2,a3)

#方式3
# 多个变量使用不同的值
v1,v2,v3 = 100,200,300
print(v1,v2,v3)