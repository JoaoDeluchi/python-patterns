from bus import Bus
from airplane import AirPlane


def main():
    travel('New York', Bus)
    travel('Amsterdam', AirPlane)


def travel(destination, transport):
    print(f'\n Taking the {transport.__name__} to {destination} ===>')

    means = transport(destination)
    means.take_trip()


if __name__ == '__main__':
    main()
