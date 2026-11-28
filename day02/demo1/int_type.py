"""
    int类型 数值类型
    type(数据/变量) 返回传入数据的类型
    isinstance()判断某个对象是否属于某个类型  返回的是bool 布尔类型
    如果属于某个类型 则结果为True  否则 结果为False

    Python中bool类继承了int 类 属于int类的子类
    面向对象思想中 子类与父类属于is-a的关系 即子类是父类 所以使用isinstance判断成立

"""

a1 = 1_000_000_000_000
print(a1)

b = 100
print(type(b)) # int

print(isinstance(b,int)) # True


c = True
print(type(c))  # bool
print(isinstance(c,bool)) # True 可以直接判断本类类型
print(isinstance(c,int)) # True 还会判断父类类型

# 在C语言中 是没有布尔类型 使用1表示True 使用0表示False Python底层实现本身就是C语言 所以继续沿用这个设计
# 但是在Python中新增一个类型 bool
print(True + 1)
print(False + 1)


print("*" * 100)

d = 100
print(isinstance(d,bool)) # False

print("*" * 100)

e = 100
f = False
# ==表示判断是否成立
print(type(e) == type(f)) # False












