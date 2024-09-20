"""
双色球随机选号程序

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""
# 导入了 random 模块中的三个函数：
# randrange：用于生成指定范围内的随机整数。
# randint：用于生成某个范围内的随机整数，包含上下限。
# sample：用于从一个列表中随机选择指定数量的不重复元素。
from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    balls：双色球号码的列表，包含 6 个红球和 1 个蓝球。
    """
    # enumerate 函数会给 balls 中的每个元素加上一个索引。
    # 遍历所有球，并格式化输出红球和蓝球。
    for index, ball in enumerate(balls):
        # 如果当前球是最后一个球（蓝球），在前面加个'|'进行分隔。
        if index == len(balls) - 1:
            print('|', end=' ')
        # 输出每个球的号码，'%02d' 确保号码是两位数字，不足两位前面补 0。
        print('%02d' % ball, end=' ')
    # 输出完当前这组号码后换行。
    print()


def random_select():
    """
    随机选择一组号码（6个红球和1个蓝球）
    """
    # 生成1到33的红球号码列表。
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # 从红球中随机选出6个不重复的号码。
    for _ in range(6):
        # 随机选择一个红球的索引。
        print(red_balls)
        print('红球的长度%d' % len(red_balls))
        index = randrange(len(red_balls))
        print('红球的索引%d' % index)
        # 将该红球加入到已选择的号码列表中。
        selected_balls.append(red_balls[index])
        print('已选择的红球%d' % selected_balls[-1])
        # 从红球列表中删除已选择的红球，防止重复选择。
        del red_balls[index]

    # 这里使用 sample 函数也可以完成上面的随机选择 6 个不重复红球的功能。
    # selected_balls = sample(red_balls, 6)

    # 将6个红球号码从小到大排序。
    selected_balls.sort()
    # 随机选择1到16之间的蓝球，并添加到选中的号码列表中。
    selected_balls.append(randint(1, 16))
    # 返回选中的红球和蓝球号码列表。
    return selected_balls


def main():
    """
    程序主函数，控制双色球号码的生成和输出。
    """
    # 获取用户输入的注数，将输入的字符串转换为整数。
    n = int(input('机选几注: '))
    # 生成并输出用户要求的 n 注号码。
    for _ in range(n):
        # 调用 random_select 随机生成一组双色球号码，并使用 display 输出。
        display(random_select())


# 如果当前文件是被直接执行，而不是被导入，那么执行 main 函数。
if __name__ == '__main__':
    main()
