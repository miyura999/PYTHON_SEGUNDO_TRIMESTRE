class animal:
    def hablar(self):
        pass


class perro(animal):
    def hablar(self):
        print("Guau!")


class gato(animal):
    def hablar(self):
        print("Miau!")


for animal in perro(), gato():
    animal.hablar()
    