import random

from pet_mediator import PetMediator

from pets.cat import Cat
from pets.dog import Dog
from pets.fish import Fish


def main():
    cat = Cat('Schrodinger')
    dog = Dog('Pluto')
    fish = Fish('Wanda')

    mediator = PetMediator(cat, dog, fish)
    cat.mediator = mediator
    dog.mediator = mediator
    fish.mediator = mediator

    t = random.randrange(-1, 2)
    mediator.time_of_day(t)


if __name__ == '__main__':
    main()
