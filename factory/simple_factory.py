from .pizza import CheesePizza, PepperoniPizza


class PizzaFactory:

    @classmethod
    def create_pizza(cls, kind):
        if kind == 'cheese':
            return CheesePizza()
        elif kind == 'pepperoni':
            return PepperoniPizza()
