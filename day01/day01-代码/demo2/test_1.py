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










