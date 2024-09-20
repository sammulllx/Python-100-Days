# 定义一个函数 gcd，用于计算两个数的最大公约数
def gcd(x, y):
    # 如果 x 比 y 大，交换 x 和 y 的值，确保 x 是较小的那个数
    if x > y:
        (x, y) = (y, x)  # 交换 x 和 y
    # 从 x 开始递减，寻找同时能整除 x 和 y 的最大因数
    for factor in range(x, 1, -1):
        # 如果 factor 同时能整除 x 和 y
        if x % factor == 0 and y % factor == 0:
            return factor  # 返回这个因数作为最大公约数
    # 如果循环结束还没有找到比 1 更大的因数，返回 1
    return 1


# 定义一个函数 lcm，用于计算两个数的最小公倍数
def lcm(x, y):
    # 最小公倍数等于 x 和 y 的乘积，除以它们的最大公约数
    return x * y // gcd(x, y)


# 测试 gcd 和 lcm 函数
print(gcd(15, 27))  # 输出 15 和 27 的最大公约数，应该是 3
print(lcm(15, 27))  # 输出 15 和 27 的最小公倍数，应该是 135
