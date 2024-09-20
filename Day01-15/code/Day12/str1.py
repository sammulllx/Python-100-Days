import pyperclip  # 导入pyperclip模块，用于操作剪贴板

# 使用转义字符 \' 来表示单引号字符
print('My brother\'s name is \'007\'')

# 使用原始字符串，r前缀让字符串中的反斜杠失去转义功能
print(r'My brother\'s name is \'007\'')

# 定义一个包含字母和数字的字符串
str = 'hello123world'

# 判断字符串中是否包含子串 'he'
print('he' in str)  # 输出：True

# 判断字符串中是否包含子串 'her'
print('her' in str)  # 输出：False

# 判断字符串是否只包含字母，结果为 False 因为其中包含数字
print(str.isalpha())  # 输出：False

# 判断字符串是否只包含字母和数字，结果为 True
print(str.isalnum())  # 输出：True

# 判断字符串是否只包含数字，结果为 False
print(str.isdecimal())  # 输出：False

# 判断字符串的前5个字符是否全是字母，结果为 True（hello）
print(str[0:5].isalpha())  # 输出：True

# 判断字符串第5到第8个字符是否全是数字，结果为 True（123）
print(str[5:8].isdecimal())  # 输出：True

# 定义一个包含古诗句子的列表
list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

# 使用 join 方法将列表中的元素用 '-' 连接成一个字符串
print('-'.join(list))  # 输出：床前明月光-疑是地上霜-举头望明月-低头思故乡

# 定义一个英文句子
sentence = 'You go your way I will go mine'

# 使用 split 方法将句子按空格分割成列表
words_list = sentence.split(' ')
print(words_list)  # 输出：['You', 'go', 'your', 'way', 'I', 'will', 'go', 'mine']

# 定义一个带有前后空格的邮箱字符串
email = '     jackfrued@126.com          '

# 原样输出邮箱
print(email)  # 输出带有空格的字符串

# 使用 strip 方法去除字符串两边的空格
print(email.strip())  # 输出：jackfrued@126.com

# 使用 lstrip 方法去除字符串左边的空格
print(email.lstrip())  # 输出：jackfrued@126.com           （右边的空格依然保留）

# 使用 pyperclip.copy 方法将文本复制到系统剪贴板
pyperclip.copy('老虎不发猫你当我病危呀')

# 从剪贴板获取文本（这行代码被注释掉了，如果需要可以取消注释）
# print(pyperclip.paste())
