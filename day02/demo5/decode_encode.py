"""
    encode() 根据指定的编码格式编码
    decode() 根据指定的解码格式解码
    编码个解码务必使用相同的编码表 否则将报错
    一个中文占几个字节？
        GBK 一个中文占2个字节
        UTF-8 一个中文占3个字节

    一个英文字母占几个字节？
        永远是一个字节


"""

s1 = "世界你好"
bytes_data = s1.encode(encoding="GBK")
print(bytes_data)


s2 = bytes_data.decode(encoding="GBK")
print(s2)