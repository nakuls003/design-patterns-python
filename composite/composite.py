from abc import ABC, abstractmethod


class OperationNotSupportedException(Exception):
    def __init__(self, message='This operation is not supported'):
        super().__init__(message)


class MenuComponent(ABC):
    def add(self, component):
        raise OperationNotSupportedException()

    def remove(self, component):
        raise OperationNotSupportedException()

    def get_child(self, i):
        raise OperationNotSupportedException()

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name, price, is_veg):
        self.name = name
        self.price = price
        self.is_veg = is_veg

    def print(self):
        print('{}, ${}'.format(self.name, self.price), '(V)' if self.is_veg else '')

    def __iter__(self):
        yield self


class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.menu_components = []

    def add(self, component):
        self.menu_components.append(component)

    def remove(self, component):
        self.menu_components.remove(component)

    def get_child(self, i):
        return self.menu_components[i]

    def print(self):
        print('\n------{}------\n'.format(self.name))
        for item in self.menu_components:
            item.print()

    def __iter__(self):
        stack = self.menu_components[::-1]
        while stack:
            component = stack.pop()
            if isinstance(component, MenuItem):
                yield component
            else:
                stack.extend(component.menu_components[::-1])


class PancakeHouseMenu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.add(MenuItem('Honey oat pancake', 2.50, True))
        self.add(MenuItem('Double egg pancake', 3.25, False))
        self.add(MenuItem('Blueberry pancake', 4.00, True))
        self.add(MenuItem('Chocolate egg pancake', 4.20, False))


class DinerMenu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.add(MenuItem('Steamed veggies', 6.50, True))
        self.add(MenuItem('Grilled Chicken breast', 8.00, False))
        self.add(MenuItem('Prawn curry', 10.25, False))
        self.add(MenuItem('Fish and chips', 7.00, False))
        self.add(DessertMenu('Desserts'))


class CafeMenu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.add(MenuItem('European pan roast', 9.00, False))
        self.add(MenuItem('Lasagna', 20.00, False))
        self.add(MenuItem('Lobster', 25.00, False))
        self.add(MenuItem('Caviar', 40.00, False))
        self.add(MenuItem('Tuna Sandwich', 12.50, False))
        self.add(MenuItem('Hummus and Pita bread', 15.00, True))
        self.add(MenuItem('Grilled Salmon', 16.75, False))


class DessertMenu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.add(MenuItem('Nutty Buddy', 5.00, True))
        self.add(MenuItem('Rum Raisin', 5.00, True))
        self.add(MenuItem('Dark Sundae', 6.00, True))


class Waitress:
    def __init__(self, menu_component):
        self.menu_component = menu_component

    def print_menu(self):
        self.menu_component.print()

    def print_vegetarian_menu(self):
        for item in self.menu_component:
            if item.is_veg:
                item.print()


if __name__ == '__main__':
    phm = PancakeHouseMenu('Pancake House Menu')
    dm = DinerMenu('Diner Menu')
    cm = CafeMenu('Cafe Menu')
    all_menu = Menu('Our delicious breakfast,lunch and dinner menu')
    all_menu.add(phm)
    all_menu.add(dm)
    all_menu.add(cm)
    w = Waitress(all_menu)
    # w.print_menu()
    w.print_vegetarian_menu()
