"""
Cracking the Coding Interview
Check if someone's move has won the game
Input:
participant moves [[x,y], [x,y], [x, y]] (each list representing a move)
board grid    = [[(0, 2),(1, 2),(2, 2)],
                 [(0, 1), (1,1),(2, 1)],
                 [(0, 0), (1, 0), (2, 0)]]
example_final_board = [["X", "X", "O"],
                       ["O", "X", "X"],
                       ["O", "X", "O"]]
input values will be X and O,
Board will remember old moves and return the first winning move
return [0,1]
"""

class UnitTest(unittest.TestCase):
    def test_vertical_winner(self):
        play = [[1, 1], [2, 1], [0, 0], [2, 2], [1, 0], [0, 1], [0, 2], [2, 0], [1, 2]]
        self.assertEqual(tic_tac_tow_winning_move(play), [2, 0])

    def test_winner_too_many_moves(self):
        play = [[1,1], [2,1], [2,0], [0,2], [1,2], [0,1], [1,0], [0,0], [2,2], [0,1], [2,2]]
        self.assertEqual(tic_tac_tow_winning_move(play), [1,0])

    def test_no_winner(self):
        play = [[1, 1], [2, 1], [2, 0], [0, 2], [1, 2], [0, 1], [0, 0], [2, 2], [0, 1]]
        self.assertEqual(tic_tac_tow_winning_move(play), 'no winner')

    def test_diagonal_winner(self):
        play = [[1,1], [2,1], [0,0], [0,2], [2,2], [0,1], [1,0], [0,0], [2,2], [0,1], [2,2]]
        self.assertEqual(tic_tac_tow_winning_move(play), [2,2])