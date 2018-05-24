class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):        
    def run(self):
        print('Dog is running...')
    
    def eat(self):
        print('Eating meat...')
        


class Cat(Animal):
    def run(self):
        print('Cat is running...')
    
dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)
