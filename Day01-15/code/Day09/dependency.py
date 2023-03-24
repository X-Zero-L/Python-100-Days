"""
对象之间的依赖关系和运算符重载

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        self._current_speed = min(self._current_speed, self._max_speed)

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s当前时速%d' % (self._brand, self._current_speed)


class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # 学生和车之间存在依赖关系 - 学生使用了汽车
    def drive(self, car):
        print(f'{self._name}驾驶着{car._brand}欢快的行驶在去西天的路上')
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print(f'{self._name}正在学习{course_name}.')

    def watch_av(self):
        if self._age < 18:
            print(f'{self._name}只能观看《熊出没》.')
        else:
            print(f'{self._name}正在观看岛国爱情动作片.')

    # 重载大于(>)运算符
    def __gt__(self, other):
        return self._age > other._age

    # 重载小于(<)运算符
    def __lt__(self, other):
        return self._age < other._age


if __name__ == '__main__':
    stu1 = Student('骆昊', 38)
    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
