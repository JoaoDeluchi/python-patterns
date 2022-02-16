from mock_vendors import MOCKVENDORS
CUSTOMERS = MOCKVENDORS


def main():
    for customer in CUSTOMERS:
        print(f'Name: {customer.name}; Address: {customer.address}')


if __name__ == '__main__':
    main()
