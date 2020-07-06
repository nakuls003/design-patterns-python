from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print('quack quack!')

    def fly(self):
        print('I\'m flying!')


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print('gobble gobble!')

    def fly(self):
        print('I\'m flying!')


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        self.turkey.fly()


def test_duck(duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    md = MallardDuck()
    test_duck(md)
    wt = TurkeyAdapter(WildTurkey())
    test_duck(wt)

