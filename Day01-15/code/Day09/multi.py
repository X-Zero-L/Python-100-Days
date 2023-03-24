"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print(f'{self._name}在打麻将.')

    def eat(self):
        print(f'{self._name}在大吃大喝.')


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print(f'{self._name}在吃斋.')

    def chant(self):
        print(f'{self._name}在念经.')


class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print(f'{self._name}在细嚼慢咽.')

    def play_piano(self):
        print(f'{self._name}在弹钢琴.')


# 试一试下面的代码看看有什么区别
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


son = Son('王大锤')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
