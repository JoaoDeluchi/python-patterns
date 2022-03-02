from abs_state import AbsState


class AtCheckOut(AbsState):
    def add_item(self):

        print('You cant add items at the check out counter')

    def remove_item(self):
        self._cart.items -= 1
        if self._cart.items:
            print('You now have {self._cart.items} items in your cart')
        else:
            print('Your cart is empty')
            self._cart.items = self._cart.empty

    def checkout(self):
        print('you´re already at checkout!')

    def pay(self):
        print('You paid for {self._cart.items} items!')
        self._cart.state = self._cart.paid_for

    def empty_cart(self):
        self._cart.items = 0
        self._cart.state = self._cart.empty
        print('You cart is empty')
