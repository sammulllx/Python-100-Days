"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

# 自定义过滤器函数
# 该函数接收一个字符串参数，并判断其长度是否为6


def myfilter(mystr):
    return len(mystr) == 6


# 使用 help() 函数可以查看函数或对象的详细帮助信息
# help()

# 使用 chr() 函数将 Unicode 编码 0x9a86 转换为对应的字符
print(chr(0x9a86))  # 输出: '骆'

# 使用 ord() 函数将字符 '骆' 转换为对应的 Unicode 编码
# 使用 hex() 函数将这个 Unicode 编码转换为十六进制字符串表示形式
print(hex(ord('骆')))  # 输出: '0x9a86'

# 使用 abs() 函数返回数字的绝对值
print(abs(-1.2345))  # 输出: 1.2345

# 使用 round() 函数对数字进行四舍五入，默认为保留到整数位
print(round(-1.2345))  # 输出: -1

# 使用 pow() 函数计算数字的幂次，即 1.2345 的 5 次方
print(pow(1.2345, 5))  # 输出: 3.1718029506252316

# 定义一个包含水果名称的列表
fruits = ['orange', 'peach', 'durian', 'watermelon']

# 使用 slice() 函数对列表进行切片操作
# slice(1, 3) 表示从索引 1 开始切到索引 3 （不包含 3）
print(fruits[slice(1, 3)])  # 输出: ['peach', 'durian']  等同fruits[1:3]


# 使用 filter() 函数过滤列表元素
# filter() 函数将 myfilter 函数应用于 fruits 列表中的每个元素，并只返回符合条件的元素
# 在这里，只有长度为6的字符串会被保留
fruits2 = list(filter(myfilter, fruits))
# 打印原始列表
print(fruits)  # 输出: ['orange', 'peach', 'durian', 'watermelon']
# 打印过滤后的新列表
print(fruits2)  # 输出: ['orange', 'durian']
