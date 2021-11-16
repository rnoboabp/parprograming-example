import unittest

from app import result_player


class TestPlayer(unittest.TestCase):

    def test_player(self):
        # Given
        player_1 = 0
        player_2 = 0

        print(result_player(player_1, player_2))


if __name__ == '__main__':
    unittest.main()
