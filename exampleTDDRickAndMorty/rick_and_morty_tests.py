import unittest
from rick_and_morty import Rick
from rick_and_morty import Morty
from rick_and_morty import Citadel
from unittest import mock


class RickTests(unittest.TestCase):

    def test_assign_universe_to_rick(self):

        # arrange
        expected_universe = 111
        rick = Rick(expected_universe)

        # act
        actual_universe = rick.universe

        # assert
        self.assertEqual(actual_universe, expected_universe)

    def test_rick_has_morty(self):

        # arrange
        rick = Rick(111)

        # act, assert
        self.assertEqual(rick.assigned_morty, None)

    def test_assign_morty_to_rick(self):

        # arrange
        rick = Rick(111)
        morty = Morty(111)

        # act
        rick.assign(morty)

        # assert
        self.assertEqual(rick.assigned_morty, morty)
        self.assertTrue(morty.is_assigned)

    @mock.patch('rick_and_morty.Morty')
    def test_assign_morty_to_rick_mock(self, morty):

        # arrange
        rick = Rick(111)

        # act
        rick.assign(morty)

        # assert
        self.assertEqual(rick.assigned_morty, morty)
        self.assertTrue(morty.is_assigned)

    def test_rick_is_not_pickle(self):

        # arrange
        rick = Rick(111)

        # act, assert
        self.assertFalse(rick.is_pickle)

    def test_rick_is_pickle(self):

        # arrange
        rick = Rick(111)
        morty = Morty(111)
        rick.assign(morty)

        # act, assert
        self.assertTrue(rick.is_pickle)

    def test_partial_mock(self):
        with mock.patch.object(Rick, 'assign', return_value=333):
            rick = Rick(111)
            self.assertEqual(rick.assign(), 333)


class MortyTests(unittest.TestCase):

    def test_assign_universe_to_morty(self):

        # arrange
        expected_universe = 111
        morty = Morty(expected_universe)

        # act
        actual_universe = morty.universe

        # assert
        self.assertEqual(actual_universe, expected_universe)

    def test_morty_is_assigned_to_rick(self):

        # arrange
        morty = Morty(111)

        # act, assert
        self.assertEqual(morty.is_assigned, False)


class CitadelTests(unittest.TestCase):

    def test_get_citadel_residents(self):

        # arrange
        expected_cit_residents = []
        citadel = Citadel()

        # act
        actual_cit_residents = citadel.get_citadel_residents()

        # assert
        self.assertEqual(actual_cit_residents, expected_cit_residents)

    def test_add_residents_to_citadel(self):

        # arrange
        citadel = Citadel()
        rick = Rick(111)
        morty = Morty(111)

        # act
        citadel.add_resident(rick)
        citadel.add_resident(morty)
        residents = citadel.get_citadel_residents()

        # assert
        self.assertEqual(residents[0], rick)
        self.assertEqual(residents[1], morty)


if __name__ == '__main__':
    unittest.main()
