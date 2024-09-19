class Person(object):
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def play(self):
        if self._age < 16:
            print('%s在玩飞行棋' % self._name)
        else:
            print('%s在玩斗地主' % self._name)


def main():
    p1 = Person('Alice', 15)
    p1.play()
    p1.age = 18
    p1._gender = 'female'

    p1.play()
    print(p1.name)
    print(p1.age)


main()
