from Board import Board
from Player import Player


class Game:
    """Main Class of the game. run this file to play the game"""

    PlayerX = Player("X")
    PlayerO = Player("O")
    Turn = PlayerX
    board = Board()

    @staticmethod
    def is_over():
        """Determines whether the game is over"""
        if Game.board.winner() is not None:
            return Game.board.winner()
        else:
            return False

    @staticmethod
    def next_turn():
        """Switches around whose turn it is"""
        if Game.Turn is Game.PlayerX:
            Game.Turn = Game.PlayerO
        else:
            Game.Turn = Game.PlayerX


while True:
    """runs as long as the game is on"""
    print("Player %s it is your turn" % Game.Turn.to_string())
    print(Game.board.pretty_print())
    raw = input("Where do you want to put your %s? Please use the Syntax: 'row column' and start counting from zero:" % Game.Turn.to_string())
    row = raw.split(" ")[0]
    col = raw.split(" ")[1]
    if Game.board.insert(int(row), int(col), Game.Turn.to_int()) is False:
        print("This position is already taken")
        continue
    if Game.is_over() is not False:
        print(Game.board.pretty_print())
        print("Congratulations Player{}! You won!".format(Game.is_over().to_string()))
        break
    Game.next_turn()
    print("\n")
    print("\n")
    print("\n")
