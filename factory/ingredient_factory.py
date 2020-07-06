from abc import ABC, abstractmethod

from factory.ingredients import ThinCrustDough, Marinara, Reggiano, BlackOlive, RedPepper, SlicedPepperoni, FreshClams, \
    ThickCrustDough, PlumTomato, Mozzarella, Spinach, Onion, CubedPepperoni, FrozenClams


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def get_dough(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_cheese(self):
        pass

    @abstractmethod
    def get_veggies(self):
        pass

    @abstractmethod
    def get_pepperoni(self):
        pass

    @abstractmethod
    def get_clams(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def get_dough(self):
        return ThinCrustDough()

    def get_sauce(self):
        return Marinara()

    def get_cheese(self):
        return Reggiano()

    def get_veggies(self):
        veggies = [BlackOlive(), RedPepper()]
        return veggies

    def get_pepperoni(self):
        return SlicedPepperoni()

    def get_clams(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def get_dough(self):
        return ThickCrustDough()

    def get_sauce(self):
        return PlumTomato()

    def get_cheese(self):
        return Mozzarella()

    def get_veggies(self):
        veggies = [Spinach(), Onion()]
        return veggies

    def get_pepperoni(self):
        return CubedPepperoni()

    def get_clams(self):
        return FrozenClams()
