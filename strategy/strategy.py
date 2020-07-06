from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I'm flying with wings")


class NoFly(FlyBehaviour):
    def fly(self):
        print("I can't fly")


class RocketPoweredFlying(FlyBehaviour):
    def fly(self):
        print("I'm flying with rocket power")


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack Quack!")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak Squeak!")


class Silence(QuackBehaviour):
    def quack(self):
        print("Can't quack")


class Duck(ABC):
    def __init__(self, fly_behaviour, quack_behaviour):
        self.fly_behaviour = fly_behaviour
        self.quack_behaviour = quack_behaviour

    def swim(self):
        print("I am swimming")

    @abstractmethod
    def display(self):
        pass

    def quack(self):
        self.quack_behaviour.quack()

    def fly(self):
        self.fly_behaviour.fly()


class MallardDuck(Duck):
    def display(self):
        print("I am a mallard duck")


class RedHeadDuck(Duck):
    def display(self):
        print("I am a redhead duck")


class RubberDuck(Duck):
    def display(self):
        print("I am a rubber duck")


class WoodenDecoyDuck(Duck):
    def display(self):
        print("I am a mallard duck")


class RocketPoweredDuck(Duck):
    def display(self):
        print("I am a rocket powered duck")


if __name__ == '__main__':
    rocket_powered_duck = RocketPoweredDuck(NoFly(), Silence())
    rocket_powered_duck.display()
    rocket_powered_duck.fly()
    rocket_powered_duck.quack()
    rocket_powered_duck.fly_behaviour = RocketPoweredFlying()
    rocket_powered_duck.fly()
