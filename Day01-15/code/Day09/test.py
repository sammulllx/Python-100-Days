'''不可变与可变的对比

	•	不可变对象（如 int、str）：函数中的修改不会影响外部的变量。
	•	可变对象（如自定义类、列表）：函数中的修改会影响外部的对象。
'''


class Test(object):
    def __init__(self, a):
        self.a = a


def test_add(obj):
    obj.a += 1
    print('a=%d' % obj.a)


def func1(a):
    a += 100
    print(a)


print(Test(11111).a)

s = Test(10)
print('a=%d' % s.a)
test_add(s)
print('a=%d' % s.a)

b = 1
func1(b)
print(b)
