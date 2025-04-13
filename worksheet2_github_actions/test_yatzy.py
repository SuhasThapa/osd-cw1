import unittest
from yatzy import Yatzy  # Assume your class is in a file called yatzy.py

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.game = Yatzy()

    def test_upper_section(self):
        self.game.dice = [MockDie(1), MockDie(1), MockDie(2), MockDie(4), MockDie(6)]
        self.assertEqual(self.game.Ones(), 2)
        self.assertEqual(self.game.Twos(), 2)
        self.assertEqual(self.game.Threes(), 0)
        self.assertEqual(self.game.Fours(), 4)
        self.assertEqual(self.game.Sixes(), 6)

    def test_one_pair(self):
        self.game.dice = [MockDie(2), MockDie(2), MockDie(3), MockDie(4), MockDie(6)]
        self.assertEqual(self.game.OnePair(), 4)

    def test_two_pairs(self):
        self.game.dice = [MockDie(2), MockDie(2), MockDie(4), MockDie(4), MockDie(6)]
        self.assertEqual(self.game.TwoPairs(), 12)

    def test_three_alike(self):
        self.game.dice = [MockDie(3), MockDie(3), MockDie(3), MockDie(5), MockDie(6)]
        self.assertEqual(self.game.ThreeAlike(), 9)

    def test_four_alike(self):
        self.game.dice = [MockDie(5), MockDie(5), MockDie(5), MockDie(5), MockDie(2)]
        self.assertEqual(self.game.FourAlike(), 20)

    def test_small_straight(self):
        self.game.dice = [MockDie(1), MockDie(2), MockDie(3), MockDie(4), MockDie(5)]
        self.assertEqual(self.game.Small(), 15)

    def test_large_straight(self):
        self.game.dice = [MockDie(2), MockDie(3), MockDie(4), MockDie(5), MockDie(6)]
        self.assertEqual(self.game.Large(), 20)

    def test_full_house(self):
        self.game.dice = [MockDie(2), MockDie(2), MockDie(3), MockDie(3), MockDie(3)]
        self.assertEqual(self.game.FullHourse(), 13)

    def test_chance(self):
        self.game.dice = [MockDie(1), MockDie(2), MockDie(3), MockDie(4), MockDie(6)]
        self.assertEqual(self.game.Chance(), 16)

    def test_yatzy(self):
        self.game.dice = [MockDie(4)] * 5
        self.assertEqual(self.game.Yatzy(), 50)


class MockDie:
    def __init__(self, value):
        self.value = value
        self.locked = False
    def __repr__(self):
        return str(self.value)

if __name__ == '__main__':
    unittest.main()
