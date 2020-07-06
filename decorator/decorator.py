from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__()
        self.description = "House Blend"

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        super(DarkRoast, self).__init__()
        self.description = "Dark Roast"

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        super(Decaf, self).__init__()
        self.description = "Decaf"

    def cost(self):
        return 1.05


class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class IcedTea(Beverage):
    def __init__(self):
        super(IcedTea, self).__init__()
        self.description = 'Iced Tea'

    def cost(self):
        return 0.75


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        super(Milk, self).__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return self.beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super(Mocha, self).__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super(Soy, self).__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super(Whip, self).__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.10


if __name__ == '__main__':
    iced_tea = IcedTea()
    print(iced_tea.get_description())
    print('$: ', iced_tea.cost())

    beverage1 = Mocha(Milk(Milk(HouseBlend())))  # double milk houseblend with mocha
    print(beverage1.get_description())
    print('$: ', beverage1.cost())

    beverage2 = Whip(Decaf())  # whipped decaf
    print(beverage2.get_description())
    print('$: ', beverage2.cost())
