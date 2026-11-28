"""
    在Python中能够当做False使用的 数据
    None
    0
    0.0
    False
    所有的空容器（空列表、空元组、空字典、空集合、空字符串）

    在IDE中灰色的代码：
        1.写了没有意义(写了却没有使用)
        2.写了执行不到

"""

if not 10 < 5:
    print("条件成立1")


if not None:
    print("条件成立2")

if not 0:
    print("条件成立3")

if not 0.0:
    print("条件成立4")

if not "":
    print("条件成立5")

if not []:
    print("条件成立6")

if not ():
    print("条件成立7")

if not {}:
    print("条件成立8")

if not set():
    print("条件成立9")


# 以上 元素 可以当做False 进行判断使用 但并不是False   使用is与False比较 结果为False 不成立
print(None is False)
print("" is False)
print([] is False)


print("程序结束")