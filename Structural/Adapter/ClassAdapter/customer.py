class Customer(object):
    def __init__(self, name, address) -> None:
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address
