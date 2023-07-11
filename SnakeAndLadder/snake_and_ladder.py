import utils

class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.moves = 0

    def move(self, newPosition):
        self.position = newPosition
        self.moves += 1

    
class Board:
    
    def __init__(self, size, snake_positon=None, ladder_position=None):
        self.size = size
        self.snake_positon = snake_positon
        self.ladder_position = ladder_position

    def movePlayer(self, player, position):
        newPosition = player.position + position
        if newPosition > self.size:
            return False, "Exceed the size for player {}".format(player.name)
        if newPosition == self.size:
            return True, "Player {} are winner".format(player.name)
        elif newPosition in self.snake_positon.keys():
            player.move(self.snake_positon[newPosition])
            return False, "Snake bite at dice {} Player {} is at position {}".format(position, player.name, player.position)
        elif newPosition in self.ladder_position.keys():
            player.move(self.ladder_position[newPosition])
            return False, "Take ladder at dice {} Player {} is at position {}".format(position, player.name, player.position)
        else:
            player.move(newPosition)
            return False, "Dice Value {} Player {} is at position {}".format(position, player.name, player.position)


class Game:

    @classmethod
    def play(self, player1, player2, board):
        while True:
            newPosition = utils.roll_dice()
            player1_turn, status = board.movePlayer(player1, newPosition)
            print(status)
            if player1_turn:
                break
            newPosition = utils.roll_dice()
            player2_turn, status = board.movePlayer(player2, newPosition)
            print(status)
            if player2_turn:
                break

        
player1 = Player("Abhishek")
player2 = Player("Ria")

board = Board(8, {7:1}, {1:6})

Game.play(player1, player2, board)
