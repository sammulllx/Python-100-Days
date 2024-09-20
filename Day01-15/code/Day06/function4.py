import time  # 导入与时间相关的模块
import shutil  # 导入用于文件和目录操作的高级模块
import os  # 导入操作系统服务相关的模块

# 获取当前时间的时间戳（自1970年1月1日以来的秒数）
seconds = time.time()
print(seconds)  # 打印时间戳，精确到秒

# 将时间戳转换为本地时间的结构化格式
localtime = time.localtime(seconds)
print(localtime)  # 打印本地时间的结构化时间（tm_year, tm_mon 等信息）

# 打印当前年份
print(localtime.tm_year)
# 打印当前月份
print(localtime.tm_mon)
# 打印当前日期
print(localtime.tm_mday)


# 将结构化时间转换为标准时间字符串表示（如: 'Sat Mar 12 14:15:21 2022'）
asctime = time.asctime(localtime)
print(asctime)  # 打印标准时间字符串

# 将结构化时间转换为指定格式的时间字符串 (例如: 年-月-日 时:分:秒)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)  # 打印自定义格式化的时间字符串

# 将指定的时间字符串（2018-1-1）解析为结构化时间
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)  # 打印解析后的结构化时间

# 使用 shutil 模块将文件从一个位置复制到另一个位置
# 将文件 'hello.py' 复制到桌面并重命名为 'first.py'
shutil.copy('/Users/sammul/Downloads/wifi.png',
            '/Users/sammul/Desktop/wangluo.png')

# 使用 os 模块执行系统命令，列出当前目录下的文件和文件夹的详细信息
os.system('ls -l')

# 改变当前的工作目录到 '/Users/Hao'
os.chdir('/Users/sammul/Desktop/')

# 再次列出当前工作目录下的文件和文件夹详细信息
os.system('ls -l')

# 使用 os 模块在当前目录中创建一个名为 'test' 的新文件夹
os.mkdir('test')

os.system('touch ikun.py')
os.system('mkdir test2')
