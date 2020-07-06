class DatabaseConnection:
    _INSTANCE = None

    def __init__(self):
        from random import randint
        print('initializing database connection: {}'.format(randint(1, 100)))

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            cls._INSTANCE = super().__new__(cls, *args, **kwargs)
        return cls._INSTANCE


if __name__ == '__main__':
    d1 = DatabaseConnection()
    d2 = DatabaseConnection()
    print(id(d1), id(d2))
