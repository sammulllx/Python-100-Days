"""
类型转换示例
- 展示了 Python 中不同数据类型之间的转换，包括 int、float、str、bool 类型。

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

# 定义一个整数变量 `a`
a = 100
# 将整数 `a` 转换为字符串，赋值给变量 `b`
b = str(a)

# 定义一个浮点数变量 `c`
c = 12.345
# 将浮点数 `c` 转换为字符串，赋值给变量 `d`
d = str(c)

# 定义一个字符串变量 `e`，内容是数字字符
e = '123'
# 将字符串 `e` 转换为整数，赋值给变量 `f`
f = int(e)

# 定义一个字符串变量 `g`，内容是小数字符
g = '123.456'
# 将字符串 `g` 转换为浮点数，赋值给变量 `h`
h = float(g)

# 定义一个布尔值变量 `i`
i = False
# 将布尔值 `i` 转换为字符串，赋值给变量 `j`
j = str(i)

# 定义一个字符串变量 `k`，内容是非空字符串
k = 'hello'
# 将字符串 `k` 转换为布尔值，赋值给变量 `m`
# 任何非空字符串都会被转换为 True
m = bool(k)

# 打印变量 `a` 的值
print(a)
# 打印变量 `a` 的数据类型，输出 <class 'int'>
print(type(a))

# 打印变量 `b` 的值
print(b)
# 打印变量 `b` 的数据类型，输出 <class 'str'>
print(type(b))

# 打印变量 `c` 的值
print(c)
# 打印变量 `c` 的数据类型，输出 <class 'float'>
print(type(c))

# 打印变量 `d` 的值
print(d)
# 打印变量 `d` 的数据类型，输出 <class 'str'>
print(type(d))

# 打印变量 `e` 的值
print(e)
# 打印变量 `e` 的数据类型，输出 <class 'str'>
print(type(e))

# 打印变量 `f` 的值
print(f)
# 打印变量 `f` 的数据类型，输出 <class 'int'>
print(type(f))

# 打印变量 `g` 的值
print(g)
# 打印变量 `g` 的数据类型，输出 <class 'str'>
print(type(g))

# 打印变量 `h` 的值
print(h)
# 打印变量 `h` 的数据类型，输出 <class 'float'>
print(type(h))

# 打印变量 `i` 的值
print(i)
# 打印变量 `i` 的数据类型，输出 <class 'bool'>
print(type(i))

# 打印变量 `j` 的值
print(j)
# 打印变量 `j` 的数据类型，输出 <class 'str'>
print(type(j))

# 打印变量 `k` 的值
print(k)
# 打印变量 `k` 的数据类型，输出 <class 'str'>
print(type(k))

# 打印变量 `m` 的值
print(m)
# 打印变量 `m` 的数据类型，输出 <class 'bool'>
print(type(m))
