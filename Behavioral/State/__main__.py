from shopping_cart import ShoppingCart


def main():
    print('====> first cart')
    cart = ShoppingCart()
    cart.add_item()
    cart.remove_item()
    cart.add_item()
    cart.add_item()
    cart.add_item()
    cart.add_item()
    cart.remove_item()
    cart.checkout()
    cart.pay()

    print('====> second cart')
    cart = ShoppingCart()
    cart.add_item()
    cart.add_item()
    cart.checkout()
    cart.empty_cart()
    cart.add_item()
    cart.checkout()
    cart.pay()

    print('====> Thy add another item, error expected')
    cart.add_item()


if __name__ == '__main__':
    main()
