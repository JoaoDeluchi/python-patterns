
from .pet_handler import PetHandler
from .cat_handler import CatHandler
from .dog_handler import DogHandler
from .fish_handler import FishHandler
from .parrot_handler import ParrotHandler


handlers_list = PetHandler()
for handler in CatHandler, DogHandler, FishHandler, ParrotHandler:
    new_handler = handler()
    handlers_list.add_successor(new_handler)
