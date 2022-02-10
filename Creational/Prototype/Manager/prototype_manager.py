from abs_prototype import AbsPrototype


class PrototypeManager(dict):
    def __setitem__(self, key, prototype) -> None:
        if issubclass(prototype, AbsPrototype):
            dict.__setitem__(self, key, prototype)
