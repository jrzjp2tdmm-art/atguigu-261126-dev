"""
    complex() 通过指定实部和虚部创建一个复数
    因为在工程电气领域 i表示电流符号 所以为了避免混淆 Python将i改为了j
"""

c1 = complex(1, 2)
print(c1)
print(c1.real)
print(c1.imag)

c2 = complex("1+2j") # 字符串中间不能有空白
print(c2)
print(c2.real)
print(c2.imag)