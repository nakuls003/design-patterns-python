from datetime import datetime


class MenuItem:
    def __init__(self, name, price, is_veg):
        self.name = name
        self.price = price
        self.is_veg = is_veg


class PancakeHouseMenu:
    def __init__(self):
        self.menu_items = []
        self.add_menu_item('Honey oat pancake', 2.50, True)
        self.add_menu_item('Double egg pancake', 3.25, False)
        self.add_menu_item('Blueberry pancake', 4.00, True)
        self.add_menu_item('Chocolate egg pancake', 4.20, False)

    def add_menu_item(self, name, price, is_veg):
        menu_item = MenuItem(name, price, is_veg)
        self.menu_items.append(menu_item)

    def __iter__(self):
        return iter(self.menu_items)


class DinerMenu:
    def __init__(self):
        self.menu_items = {}
        self.add_menu_item('Steamed veggies', 6.50, True)
        self.add_menu_item('Grilled Chicken breast', 8.00, False)
        self.add_menu_item('Prawn curry', 10.25, False)
        self.add_menu_item('Fish and chips', 7.00, False)

    def add_menu_item(self, name, price, is_veg):
        menu_item = MenuItem(name, price, is_veg)
        self.menu_items[menu_item.name] = menu_item

    def __iter__(self):
        return iter(self.menu_items.values())


class CafeMenu:
    def __init__(self):
        self.menu_items = []
        self.add_menu_item('European pan roast', 9.00, False)
        self.add_menu_item('Lasagna', 20.00, False)
        self.add_menu_item('Lobster', 25.00, False)
        self.add_menu_item('Caviar', 40.00, False)
        self.add_menu_item('Tuna Sandwich', 12.50, False)
        self.add_menu_item('Hummus and Pita bread', 15.00, True)
        self.add_menu_item('Grilled Salmon', 16.75, False)

    def add_menu_item(self, name, price, is_veg):
        menu_item = MenuItem(name, price, is_veg)
        self.menu_items.append(menu_item)

    def __iter__(self):
        """
        menu items shown depend on the day of the week.
        some will be shown on Mon, Wed, Fri, Sun while others will be shown on Tue, Thu, Sat.
        """
        day_of_week = datetime.today().weekday()
        for index in range(day_of_week % 2, len(self.menu_items), 2):
            yield self.menu_items[index]


class Waitress:
    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        for menu in self.menus:
            self._print_menu(menu)

    def _print_menu(self, menu):
        for item in menu:
            print('{}, ${}'.format(item.name, item.price), '(V)' if item.is_veg else '')


if __name__ == '__main__':
    phm = PancakeHouseMenu()
    dm = DinerMenu()
    cm = CafeMenu()
    w = Waitress([phm, dm, cm])
    w.print_menu()
