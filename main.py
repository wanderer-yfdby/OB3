# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} питается")
    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("кля кля кля")


class Mammal(Animal):
    def make_sound(self):
        print("ааав")


class Reptile(Animal):
    def make_sound(self):
        print("Гену не видели?")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Зоопарк пополнился новым питомцем: {animal.name}. Ему {animal.age} лет ")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"В зоопарк устроился новый сотрудник: {new_staff}")


class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}")


class Veterinarian():
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}")


bird1 = Bird("Лебедь", 7)
reptile1 = Reptile("Крокодил", 49)
mammal1 = Mammal("Бегемот", 15)

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(mammal1)
veterinarian.heal_animal(reptile1)

mammal1.eat()
reptile1.make_sound()