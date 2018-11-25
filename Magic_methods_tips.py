class User:
    # Метод отвечающий за инициализацию созданного объекта
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }

    # Метод определяет поведение при вызове print
    # должен определять человекочитаемое описание
    def __str__(self):
        return '{0} <{1}>'.format(self.name, self.email)

    # Метод определяющий поведение при вызове функции hash(o)
    def __hash__(self):
        return hash(self.name + self.email)

    # Метод вызываемый при сравнении двух объектов
    def __eq__(self, other):
        return self.email == other.email and \
               self.name == other.name

    # Метод вызываемый в том случае, если атрибут не найден
    def __getattr__(self, item):
        return f'Attribute {item} not found!'

    # Метод вызываемый при обращении к любому атрибуту
    def __getattribute__(self, item):
        print(f'Looking for {item}...')
        return super(User, self).__getattribute__(item)

class Singleton:
    instance = None

    # Метод описывающий, что происходит в момент создания
    # объекта
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

class Logger:

    counter = 0

    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            self.counter += 1
            with open(self.filename, 'a') as f:
                f.write(f'{self.counter} Function {func} was called!\n')

            return func(*args, **kwargs)
        return wrapped

users = []

users.append(User('Sasha', 'sasha@mail.ru'))
users.append(User('Sasha1', 'sasha@mail.ru'))

for _ in users:
    print(_.get_email_data())
print('Используется __str__. Результат: {}'.format(users[0]))
print('Используется __eq__. Результат: {}'.format(users[1] == users[0]))
print('Используется __hash__. Результат: {}'.format(hash(users[0])))
print(users[0].age)

a = Singleton()
b = Singleton()
print(a is b)

logger = Logger('log.txt')

@logger
def dummy_func1():
    pass

@logger
def dummy_func2():
    pass


dummy_func1()
dummy_func2()
dummy_func1()