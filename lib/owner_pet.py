class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    sorted = all.sort()

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.__class__.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if pet.pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet: pet.name)
