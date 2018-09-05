class Some:
    # Свойство класса
    some_prop = "Property of Some class"

    # Метод класса
    @classmethod
    def print_some(cls):
        print(cls.some_prop)

    # Статический метод
    @staticmethod
    def some_static():
        print("I'm a static class method!")

    # Конструктор класса
    def __init__(self, fprop, sprop=0):
        # Свойства экземпляров класса
        self.fprop = fprop
        self.sprop = sprop

    # Методы класса
    def get_fprop(self):
        return self.fprop

    def get_sprop(self):
        return self.sprop

# Класс потомок класса Some
class InhSome(Some):

    def __init__(self, fprop, sprop, thprop):
        super().__init__(fprop, sprop)
        self.thprop = thprop
        # Скрытое свойство
        self._magic_number = 11

    def get_thprop(self):
        return self.thprop

    def __repr__(self):
        return "Magic number is: {}".format(self._magic_number)


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Магический метод который возвращает
    # Вектор равный сумме векторов v1 + v2
    def __add__(self, other):
        return Vector(self.x + other.x, self.x + other.y)

    @property
    def is_zero(self):
        return self.x == 0 & self.y == 0

    @is_zero.setter
    def is_zero(self, value):
        if value:
            self.x = 0
            self.y = 0

# Создание объектов класса Some
obj1 = Some(1, 2)
obj2 = Some(3)
print(obj1.get_fprop(), obj1.get_sprop())
print(obj2.get_fprop(), obj2.get_sprop())
# Свойство some_prop относиться ко всем объектам класса Some
print("Свойство someprop экземпляра obj1: {}".format(obj1.some_prop))
print("Свойство someprop экземпляра obj2: {}".format(obj2.some_prop))
Some.some_prop = "Property of Some class was modified"
print("Свойство someprop экземпляра obj1: {}".format(obj1.some_prop))
print("Свойство someprop экземпляра obj2: {}".format(obj2.some_prop))
obj3 = InhSome(4, 5, 6)
print(obj3.get_fprop(), obj3.get_sprop(), obj3.get_thprop())
print("Свойство someprop экземпляра obj3: {}".format(obj3.some_prop))
print(obj3)
Some.print_some()
Some.some_static()
InhSome.print_some()
InhSome.some_static()
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y)
print(v3.is_zero)
v3.is_zero = True
print(v3.is_zero)