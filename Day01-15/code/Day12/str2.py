from io import StringIO  # 导入StringIO模块，用于处理可变字符串

# 方法1: 使用Python的切片功能实现字符串倒转


def reverse_str1(str):
    # 切片操作，倒序输出字符串
    return str[::-1]


# 方法2: 使用递归方式实现字符串倒转
def reverse_str2(str):
    # 如果字符串长度小于等于1，直接返回字符串
    if len(str) <= 1:
        return str
    # 递归调用，将字符串从第二个字符开始递归处理，再加上第一个字符
    return reverse_str2(str[1:]) + str[0:1]


# 方法3: 使用StringIO对象来处理字符串倒转
def reverse_str3(str):
    # StringIO对象是一个可变字符串对象，适合用来避免频繁的字符串拼接
    rstr = StringIO()
    str_len = len(str)  # 获取字符串的长度
    # 使用for循环从字符串末尾向前遍历，将每个字符依次写入StringIO对象
    for index in range(str_len - 1, -1, -1):
        rstr.write(str[index])
    # 返回拼接好的字符串
    return rstr.getvalue()


# 方法4: 使用生成器表达式和join函数倒转字符串
def reverse_str4(str):
    # 使用生成器表达式遍历字符串的下标，从最后一个字符开始到第一个字符
    # join方法用于将字符连接成一个新的字符串
    return ''.join(str[index] for index in range(len(str) - 1, -1, -1))


# 方法5: 使用列表和zip函数实现字符串倒转
def reverse_str5(str):
    # 将字符串转换为列表，因为字符串是不可变的，而列表是可变的
    str_list = list(str)
    str_len = len(str)  # 获取字符串长度
    # zip函数用于将两个序列配对，第一个序列从前往后遍历，第二个序列从后往前遍历
    # 通过zip生成的下标对来交换字符串的前后字符
    for i, j in zip(range(str_len // 2), range(str_len - 1, str_len // 2, -1)):
        str_list[i], str_list[j] = str_list[j], str_list[i]  # 交换字符
    # 将列表中的字符重新连接成字符串
    return ''.join(str_list)


if __name__ == '__main__':
    str = 'I love Python'  # 定义测试字符串
    # 使用不同的倒转方法并输出结果
    print(reverse_str1(str))  # 调用方法1
    print(str)  # 原字符串不会被改变
    print(reverse_str2(str))  # 调用方法2
    print(str)  # 原字符串不会被改变
    print(reverse_str3(str))  # 调用方法3
    print(str)  # 原字符串不会被改变
    print(reverse_str4(str))  # 调用方法4
    print(str)  # 原字符串不会被改变
    print(reverse_str5(str))  # 调用方法5
    print(str)  # 原字符串不会被改变
