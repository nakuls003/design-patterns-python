def singleton(_class):
    _instances_dict = {}

    def wrapper(*args, **kwargs):
        if _class not in _instances_dict:
            _instances_dict[_class] = _class(*args, **kwargs)
        return _instances_dict[_class]
    return wrapper


@singleton
class DatabaseConnection:
    def __init__(self):
        from random import randint
        print('initializing database connection: {}'.format(randint(1, 100)))


if __name__ == '__main__':
    d1 = DatabaseConnection()
    d2 = DatabaseConnection()
    print(id(d1), id(d2))
