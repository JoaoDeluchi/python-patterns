

from datetime import datetime
from annual import Annual
from discount import CorporateDiscount, NoDiscount, StudentDiscount
from monthly import Monthly
from extend import Extend


def main():
    sub1 = Monthly('Ted', datetime.today(), StudentDiscount)
    sub2 = Annual('Alice', datetime.today(), CorporateDiscount)
    sub3 = Annual('Bob', datetime.today(), NoDiscount)
    print(f'{sub1.subscriber}, Cost: {sub1.price}, Expiration: {sub1.expiration}')
    print(f'{sub2.subscriber}, Cost: {sub2.price}, Expiration: {sub2.expiration}')
    print(f'{sub3.subscriber}, Cost: {sub3.price}, Expiration: {sub3.expiration}')


if __name__ == '__main__':
    main()
