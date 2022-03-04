import random
from ihearth42 import IHeart42


def main():
    g = IHeart42('Arthur')
    print(f'Hero: {g.game_state.name}, game level:{g.game_state.level}')
    memento = g.create_memento()

    g.game_state.level = random.randint(1, 42)
    g.game_state.name = 'Ford'
    print(f'Hero: {g.game_state.name}, game level:{g.game_state.level}')

    g.set_memento(memento)
    print(f'Hero: {g.game_state.name}, game level:{g.game_state.level}')


if __name__ == '__main__':
    main()
