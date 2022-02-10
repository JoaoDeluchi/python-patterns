from .abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevrolet Volt Running with shocking power!')

    def stop(self):
        print('Chevrolet Volt shutting down.')
