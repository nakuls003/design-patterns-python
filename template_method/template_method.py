from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print('Boiling water')

    def pour_in_cup(self):
        print('Pouring beverage in cup')

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_wants_condiments(self):
        return True


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Brewing coffee grind')

    def add_condiments(self):
        print('Adding milk and sugar')

    def customer_wants_condiments(self):
        choice = input('Do you want milk and sugar in your coffee? (reply Y/N)')
        return choice.lower() == 'y'


class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping tea leaves')

    def add_condiments(self):
        print('Adding lemon')


if __name__ == '__main__':
    t = Tea()
    c = Coffee()
    t.prepare_recipe()
    c.prepare_recipe()
