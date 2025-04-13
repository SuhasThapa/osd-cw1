import random

class Die:
    def __init__(self):
        self.value = 1
        self.locked = False
        self.roll()

    def roll(self):
        if not self.locked:
            self.value = random.randint(1, 6)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def __repr__(self):
        return f"{'[L]' if self.locked else '[ ]'}{self.value}"


class Yatzy:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.roll()  # Roll all dice on creation

    def roll(self):
        for die in self.dice:
            die.roll()

    def get_values(self):
        return [die.value for die in self.dice]

    def lock_dice(self, indices):
        for i in indices:
            if 0 <= i < len(self.dice):
                self.dice[i].lock()

    def unlock_all(self):
        for die in self.dice:
            die.unlock()

    def _count_values(self):
        values = self.get_values()
        return {x: values.count(x) for x in set(values)}

    def Ones(self): return self.get_values().count(1) * 1
    def Twos(self): return self.get_values().count(2) * 2
    def Threes(self): return self.get_values().count(3) * 3
    def Fours(self): return self.get_values().count(4) * 4
    def Fives(self): return self.get_values().count(5) * 5
    def Sixes(self): return self.get_values().count(6) * 6

    def OnePair(self):
        counts = self._count_values()
        pairs = [v for v, c in counts.items() if c >= 2]
        return max(pairs)*2 if pairs else 0

    def TwoPairs(self):
        counts = self._count_values()
        pairs = sorted([v for v, c in counts.items() if c >= 2], reverse=True)
        if len(pairs) >= 2:
            return pairs[0]*2 + pairs[1]*2
        return 0

    def ThreeAlike(self):
        counts = self._count_values()
        for v, c in counts.items():
            if c >= 3:
                return v * 3
        return 0

    def FourAlike(self):
        counts = self._count_values()
        for v, c in counts.items():
            if c >= 4:
                return v * 4
        return 0

    def Small(self):
        if sorted(self.get_values()) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def Large(self):
        if sorted(self.get_values()) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def FullHourse(self):
        counts = self._count_values()
        has_three = any(c == 3 for c in counts.values())
        has_two = any(c == 2 for c in counts.values())
        if has_three and has_two:
            return sum(self.get_values())
        return 0

    def Chance(self):
        return sum(self.get_values())

    def Yatzy(self):
        values = self.get_values()
        if all(v == values[0] for v in values):
            return 50
        return 0

    def display_dice(self):
        return ' '.join(str(die) for die in self.dice)