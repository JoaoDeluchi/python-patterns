from .abs_auto import AbsAuto


class FordFusion(AbsAuto):
    def start(self):
        print('Cool Ford Fusion Running smoothly!')

    def stop(self):
        print('Ford Fusion shutting down.')
