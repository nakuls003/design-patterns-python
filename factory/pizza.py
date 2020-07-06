from abc import abstractmethod, ABC


class Pizza(ABC):
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies = None
        self.pepperoni = None
        self.clams = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Putting it in the oven at 350 for 15 minutes')

    def cut(self):
        print('Cutting into diagonal slices')

    def box(self):
        print('Boxing into PizzaStore branded boxes')

    def __str__(self):
        return self.name


class CheesePizza(Pizza):
    def __init__(self, ingredients_factory):
        self.ingredients_factory = ingredients_factory
        super(CheesePizza, self).__init__('Cheese Pizza')

    def prepare(self):
        self.dough = self.ingredients_factory.get_dough()
        self.sauce = self.ingredients_factory.get_sauce()
        self.cheese = self.ingredients_factory.get_cheese()
        print('preparing cheese pizza with {}, {}, {}'.format(self.dough, self.sauce, self.cheese))


class PepperoniPizza(Pizza):
    def __init__(self, ingredients_factory):
        self.ingredients_factory = ingredients_factory
        super(PepperoniPizza, self).__init__('Pepperoni Pizza')

    def prepare(self):
        self.dough = self.ingredients_factory.get_dough()
        self.sauce = self.ingredients_factory.get_sauce()
        self.cheese = self.ingredients_factory.get_cheese()
        self.pepperoni = self.ingredients_factory.get_pepperoni()
        self.clams = self.ingredients_factory.get_clams()
        print('preparing pepperoni pizza with {}, {}, {}, {}, {}'\
              .format(self.dough, self.sauce, self.cheese, self.pepperoni, self.clams))

