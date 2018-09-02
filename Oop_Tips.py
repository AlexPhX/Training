class Some:
    # Свойство класса (static)
    some_prop = "Property of Some class"

    # Конструктор класса
    def __init__(self, fprop, sprop = 0):
        # Свойства экземпляров класса
        self.fprop = fprop
        self.sprop = sprop

    def get_fprop(self):
        return self.fprop

    def get_sprop(self):
        return self.sprop

class Inh_some(Some):

    def __init__(self, fprop, sprop, thprop):
        super().__init__(fprop, sprop)
        self.thprop = thprop

    def get_thprop(self):
        return self.thprop

# Создание объектов класса Some
obj1 = Some(1, 2)
obj2 = Some(3)
print(obj1.get_fprop(), obj1.get_sprop())
print(obj2.get_fprop(), obj2.get_sprop())
# Свойство some_prop относиться ко всем объектам класса Some
print("Свойство someprop экземпляра obj1: {}".format(obj1.some_prop))
print("Свойство someprop экземпляра obj2: {}".format(obj2.some_prop))
# Свойство someprop экземпляра obj1: Property of Some class
# Свойство someprop экземпляра obj2: Property of Some class

Some.some_prop = "Property of Some class was modified"

print("Свойство someprop экземпляра obj1: {}".format(obj1.some_prop))
print("Свойство someprop экземпляра obj2: {}".format(obj2.some_prop))
# Свойство someprop экземпляра obj1: Property of Some class was modified
# Свойство someprop экземпляра obj2: Property of Some class was modified

obj3 = Inh_some(4, 5, 6)
print(obj3.get_fprop(), obj3.get_sprop(), obj3.get_thprop())
print("Свойство someprop экземпляра obj3: {}".format(obj3.some_prop))