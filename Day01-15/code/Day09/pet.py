from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print(f'{self._nickname}: 汪汪汪...')


class Cat(Pet):

    def make_voice(self):
        print(f'{self._nickname}: 喵...喵...')


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
