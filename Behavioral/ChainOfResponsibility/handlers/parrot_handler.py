from .pet_handler import PetHandler


class ParrotHandler():
    def handle(self, request):
        if request.request_type == 'parrot':
            print('I Know a dead parrot when I see one')
            return True
