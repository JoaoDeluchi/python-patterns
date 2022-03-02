from abs_state import AbsState


class PaidFor(AbsState):
    def add_item(self):
        print('You already paid for your purchases. Want to shop some more? Get a new shopping cart')

    def remove_item(self):
        print('You already paid for your purchases and cant remove items')

    def checkout(self):
        print('Why are you back here? You alread paid.')

    def pay(self):
        print('You already paid for your purchases. You cant paid twice!')

    def empty_cart(self):
        print('You paid already.')
