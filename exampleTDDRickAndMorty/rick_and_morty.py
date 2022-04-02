class Rick:

    def __init__(self, universe):
        self.universe = universe
        self.assigned_morty = None
        self._is_pickle = False

    @property
    def is_pickle(self):
        if self.assigned_morty is not None:
            self._is_pickle = True
        else:
            self._is_pickle = False
        return self._is_pickle

    def assign(self, morty):
        self.assigned_morty = morty
        morty.is_assigned = True


class Morty:

    def __init__(self, universe):
        self.universe = universe
        self.is_assigned = False


class Citadel:

    def __init__(self):
        self._residents = []

    def get_citadel_residents(self):
        return self._residents

    def add_resident(self, resident):
        self._residents.append(resident)
