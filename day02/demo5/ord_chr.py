"""
    shift + alt + ↑↓ 上下移动当前行代码
    ord() 将字符转换为ASCII数值
    chr() 将ASCII数值转换为对应的字符

    Unicode编码表 (规范) 万国码 是一个十六进制的编码表 收录了世界上绝大多数国家的文字
    取值范围 0000 ~ FFFF (0 ~ 65535) 即这个编码一共收录了了65536个字符
    中文的取值范围是 4E00 ~ 9FA5  (19968 ~ 40869)

        UTF-8 Unicode编码规范的具体实现
        GB2312 国标标准版  收录了绝大多种中文汉字简体
        GBK 国标扩展版   收录了绝大多种中文汉字简体 以及 繁体


"""
print(ord('中'))
print(ord('你'))
print(ord('国'))

print(ord('A'))
print(ord('B'))
print(ord('C'))
print(ord('D'))

print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(ord('0'))

print("-" * 100)

print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(48))
print(chr(19968))
print(chr(19969))
print(chr(40869))
print(chr(40870))
print(chr(50000))

print("-" * 100)

