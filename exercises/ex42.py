# animal is-a object
class Animal(object):
    pass


# dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # dog has-a
        self.name = name


# cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        # cat has-a
        self.name = name


# person is-a object
class Person(object):

    def __init__(self, name):
        # person has-a name
        self.name = name

        # person has-a pet
        self.pet = None


# employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # employee is-a.
        super(Employee, self).__init__(name)
        # employee has-a salary
        self.salary = salary


# fish is-a object
class Fish(object):
    pass


# salmon is-a fish
class Salmon(Fish):
    pass


# halibut is-a fish
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# mary has-a pet, pet is-a cat, pet has-a name
mary.pet = satan

# frank is-a employee.
frank = Employee("Frank", 120000)

# frank has-a pet, pet is-a dog, dog has-a name
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
