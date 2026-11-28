"""
    bool 布尔 boolean   表示真True 或者假False
    True以及False 在Python属于特殊的对象 属于全局单例对象 GSI Global Single Instance
    表示在整个Python进程中 所有的True都是内存中的同一个对象 所有的False也是
    因为bool不可变 所以可以被共享
"""


n1 = None
n2 = None
print(n1 is n2)

print("-" * 100)

f1 = False
f2 = False
print(f1 is f2)


b1 = True
b2 = True
b3 = True

print(b1 is b2)
print(b2 is b3)



b4 = False
print(b1, b2)

b3 = 10 < 5
print(b3) # False

# 当我们使用True 或者 False 进行数学计算 Python解释器会先将True转换为1 False 转换为0 然后再进行计算
print(True + 1)
print(False + 1)


print("*" * 100)

print(True == 1)
print(False == 0)

# SyntaxWarning: "is" with 'int' literal. Did you mean "=="? 不推荐使用is比较int类型的数值
# print(True is 1) # False
# print(False is 0) # False



