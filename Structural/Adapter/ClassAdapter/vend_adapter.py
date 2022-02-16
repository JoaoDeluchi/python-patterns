from customer import Customer
from vendor import Vendor


class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return f'{self.number} {self.street}'
