class Cat:
    def __init__(self, name, age, coat_colour):
        self.name = name
        self.age = age
        coat_colour = coat_colour
    def meow(self):
        print(f'{self.name} says "Meow"')
    def purr(self):
        print(f'{self.name} purrs')
    def meet(self, other):
        if isinstance(other, Cat):
            print(f'{self.name} hisses at {other.name}')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name} barks')
    def meet(self, other):
        if isinstance(other, Cat):
            print(f'{self.name} barks at {other.name}')
        else:
            print(f'{self.name} wags its tail at {other.name}')

#Cat class section
print('Using the Cat class')
cat = Cat('Charles I', 3, 'tuxedo')
print(cat.name)
print(cat.age)

cat2 = Cat('Charles II', 4, 'tabby')
print(cat2.purr())

#dog class section
print()

print('Using the Dog class')
dog = Dog('Dasha', 6)
dog2 = Dog('Charlie', 3)

print(dog.name)
print(dog.age)
print(dog.bark())

print(cat.meet(cat2))
print(dog.meet(cat))
print(dog.meet(dog2))