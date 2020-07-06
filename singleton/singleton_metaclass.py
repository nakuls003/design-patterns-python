class Singleton(type):
    _INSTANCES_DICT = {}

    def __call__(cls, *args, **kwargs):
        if not cls in cls._INSTANCES_DICT:
            cls._INSTANCES_DICT[cls] = super().__call__(*args, **kwargs)
        return cls._INSTANCES_DICT[cls]


class DatabaseConnection(metaclass=Singleton):
    def __init__(self):
        from random import randint
        print('initializing database connection: {}'.format(randint(1, 100)))


if __name__ == '__main__':
    d1 = DatabaseConnection()
    d2 = DatabaseConnection()
    print(id(d1), id(d2))
