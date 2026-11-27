## day01

### 1. 计算机的组成

### 2. 执行Python代码的三种方式

* 在DOS命令窗口中交互模式执行
  * (Disk Operation System : 磁盘操作系统)是是一种纯命令方式的用于操作磁盘系统
* 脚本执行。需要先编写一个.py文件，然后通过python命令执行。
* 在PyCharm中编写.py文件执行。

### 3. 配置环境变量的作用

> 我们安装好Python解释器，选择了添加环境变量会自动将以下两个目录添加到系统的环境变量中
>
> C:\Users\WHD\AppData\Local\Programs\Python\Python313\Scripts
>
> C:\Users\WHD\AppData\Local\Programs\Python\Python313
>
> 有了这个动作之后，我们就可以下DOS命令窗口中输入python pip 等命令了 操作系统会自动去以上两个目录中查找到
>
> 我们所需要执行的命令，我们也可以不配置环境变量，不用上python解释器的使用，只不过在DOS窗口中将无法识别
>
> python 以及 pip命令了   



### 4. 注释

#### 4.1 单行注释

>  单行注释 以#号开头

#### 4.2 多行注释

> 多行注释左右两边各三个单引号或者双引号 不能嵌套 

```python
"""
    注释
   
    多行注释本质属于Python中的str类型的字符串对象

    ctrl + D 复制当前行代码
    ctrl + Z 撤销上一步操作
    ctrl + C 复制
    ctrl + V 粘贴
    ctrl + X 剪切并且复制
    ctrl + / 注释/取消注释  选中的代码 
"""
# 这行代码用于打印输出一句话 print属于python提供的函数 hello pycharm属于我们传入的参数 属于字符串 str类型
# print("hello pycharm") 这行代码将不再执行


print(1)
print(2)
print(3)
print(4)
print(5)
```

### 5. 字符串

```python
"""
    多行文本 字符串对象
    Python中的字符串有三种写法
    单引号 双引号 三对双引号包括

    在Python中 万物皆对象 任何数据都是对象  在内存中存放  堆heap
    堆属于内存中的一块区域 专门用于存放对象

"""

s1 = 'a'
s2 = "b"
s3 = """c"""

print(s1)
print(s2)
print(s3)

s4 = '<!DOCTYPE html>\
<html lang="en">\
<head>\
    <meta charset="UTF-8">\
    <title>Title</title>\
</head>\
<body>\
\
</body>\
</html>'

s5 = "<!DOCTYPE html>\
<html lang='en'>\
<head>\
    <meta charset='UTF-8'>\
    <title>Title</title>\
</head>\
<body>\
\
</body>\
</html>"

# 在Java语言中 这种属于文本段  JDK14新增的新特性
# 在python中依然属于字符串 特别用于保存一些结构性比较强的文本
s6 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
"""
```

### 6. 变量的创建

```python
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
```

### 7. 变量的修改

```python
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

```



### 8. 常量

> 常量：constant  不能改变的数据属于常量
> 在程序中 有一些数据是固定的 不允许随意修改 那么 可以将其设定为常量
> 对于常量 按照编码规范 名称必须全部大写(为了更加醒目) 多个单词之间下划线分割
> Python中的常量 全靠开发人员自觉遵守 不具备约束性
>
> **字面量(Literal)属于常量**

```python
"""
   常量：constant  不能改变的数据属于常量
   在程序中 有一些数据是固定的 不允许随意修改 那么 可以将其设定为常量
   对于常量 按照编码规范 名称必须全部大写(为了更加醒目) 多个单词之间下划线分割
   Python中的常量 全靠开发人员自觉遵守 不具备约束性
"""

radius = 10
PI = 3.14
PI = 3.24 # 这里还可以修改 但是不推荐修改

print(PI * radius * radius)

PERSON_COUNTRY  = "中国"



```

### 9. 单位换算

* 1TB = 1024GB
* 1GB = 1024MB
* 1MB = 1024KB
* 1KB = 1024Byte(字节)
* 1Byte = 8bit(位)

一个字节占8位，每一位只能存一个0或者一个1，位即为计算器中最小的存储单位了。

### 10. 各种进制的整数赋值方式

```python
"""
    各种进制整数的赋值方式
"""

# 二进制 0b 或者 0B开头

a = 0B11
print(a)

b = 0O11
print(b)

c = 100
print(c)

d = 0X11
print(d)

e = 0X4E2D # 20013
print(e)

f = 0X4E00 # 19968 中文汉字 一
print(f)

g = 0X9FA5 # 40869 中文汉字
print(g)

print("*" * 50)

a1 = 3
print(bin(a1)) # bin binary 二进制 转换为二进制

a2 = 9
print(oct(a2))

a3 = 17
print(hex(a3))

```

