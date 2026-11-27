"""
    标识符的命名规范
    只能包含字母、数字和下划线，且不能以数字开头。
    区分大小写，即Name和name是两个不同的标识符。
    不要和关键字重复。
    应既简短又具有描述性。
    注意：Python源文件不遵循命名规范不影响程序的执行，但不建议

    ctrl + alt + L 自动对齐代码

"""

a = 'abc'
print(a)

a1 = 100
print(a1)

a2b3c4 = 100
print(a2b3c4)

_d = 100
print(_d)

d_ = 200
print(d_)


studentName = "赵四" # 这种属于小写驼峰 Java语言采用
print(studentName)


stu_name = "大拿" # 这种属于蛇形命名法 Python官方推荐
print(stu_name)


class StudentInfo:
    pass
