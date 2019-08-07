from bowling import Bowling
from unittest import TestCase

class BowlingTest(TestCase):

    def test_the_score_is_the_sum_of_the_frames_one_frame(self):
        frames = [[1,8],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.assertEqual(Bowling().new_score(frames), 9)

    def test_the_score_is_the_sum_of_the_frames_two_frames(self):
        frames = [[1,8],[1,2],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.assertEqual(Bowling().new_score(frames), 12)

    def test_the_score_is_the_sum_of_the_frames(self):
        frames = [[1,8],[1,8],[1,8],[1,8],[1,8],[1,8],[1,8],[1,8],[1,8],[1,8]]
        self.assertEqual(Bowling().new_score(frames), 90)

    def test_score_the_first_spare(self):
        frames = [[1,9], [8,0]]
        self.assertEqual(Bowling().new_score(frames), 26)

    def test_score_the_first_strike(self):
        frames = [[10, 0], [8,0], [8,0]]
        self.assertEqual(Bowling().new_score(frames), 42)

    def test_prefect_game(self):
        frames = [[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 10]]
        self.assertEqual(Bowling().new_score(frames), 300)
