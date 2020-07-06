from abc import ABC, abstractmethod

from factory.ingredient_factory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from factory.pizza import PepperoniPizza, CheesePizza


class PizzaStore(ABC):
    def order_pizza(self, kind):
        my_pizza = self.create_pizza(kind)
        my_pizza.prepare()
        my_pizza.bake()
        my_pizza.cut()
        my_pizza.box()
        return my_pizza

    @abstractmethod
    def create_pizza(self, kind):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, kind):
        ingredients_factory = NYPizzaIngredientFactory()
        if kind == 'cheese':
            return CheesePizza(ingredients_factory)
        elif kind == 'pepperoni':
            return PepperoniPizza(ingredients_factory)


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, kind):
        ingredients_factory = ChicagoPizzaIngredientFactory()
        if kind == 'cheese':
            return CheesePizza(ingredients_factory)
        elif kind == 'pepperoni':
            return PepperoniPizza(ingredients_factory)
