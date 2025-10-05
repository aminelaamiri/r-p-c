import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class UnitTests(unittest.TestCase):
    def test_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreater(result, 0.60, "Échec contre Quincy")

    def test_abbey(self):
        result = play(player, abbey, 1000)
        self.assertGreater(result, 0.60, "Échec contre Abbey")

    def test_kris(self):
        result = play(player, kris, 1000)
        self.assertGreater(result, 0.60, "Échec contre Kris")

    def test_mrugesh(self):
        result = play(player, mrugesh, 1000)
        self.assertGreater(result, 0.60, "Échec contre Mrugesh")

if __name__ == "__main__":
    unittest.main()
