"""
检查变量的类型

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = 100
b = 1000000000000000000
c = 12.345
d = 1 + 5j
e = 'A'
f = 'hello, world'
g = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(d)
d = 1 + 5j

# 获取实部
print(d.real)  # 输出 1.0

# 获取虚部
print(d.imag)  # 输出 5.0

# 复数的共轭
print(d.conjugate())  # 输出 (1-5j)

# 复数加法
z = d + (3 + 2j)
print(z)  # 输出 (4+7j)
print(type(e))
print(type(f))
print(type(g))
