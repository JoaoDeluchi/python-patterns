from abs_state import AbsState


class Empty(AbsState):
    def add_item(self):
        self._cart.items += 1
        print('You added a item')
        self._cart.state = self._cart.not_empty

    def remove_item(self):
        print('You cart is empty! Nothing to remove!!')

    def checkout(self):
        print('You cart is empty! Go Shopping!!')

    def pay(self):
        print('You cart is empty. How did you get here?')

    def empty_cart(self):
        print('You cart is already empty. ')
