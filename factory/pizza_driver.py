from factory.pizza_store import PizzaStore, NYPizzaStore, ChicagoPizzaStore

if __name__ == '__main__':
    ny_pizza_store = NYPizzaStore()
    chicago_pizza_store = ChicagoPizzaStore()
    ny_pizza_store.order_pizza('cheese')
    print()
    chicago_pizza_store.order_pizza('pepperoni')