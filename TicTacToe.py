
class Board:
    def __init__(self):
        self.state = [0,0,0,0,0,0,0,0,0]
        self.players = []
        self.activePlayer = ""
    def is_board_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True
    def changeActivePlayer(self):
        if self.activePlayer == self.players[0]:
            self.activePlayer = self.players[1]
        else:
            self.activePlayer = self.players[0]
    def sign_to_printable(self, sign):
        signs = {
            0: " ",
            1: "X",
            2: "O"
        }
        return signs[sign]
   
    def checkWin(self):
        if self.state[0] == self.state[1] == self.state[2] != 0:
            return True
        elif self.state[3] == self.state[4] == self.state[5] != 0:
            return True
        elif self.state[6] == self.state[7] == self.state[8] != 0:
            return True
        elif self.state[0] == self.state[3] == self.state[6] != 0:
            return True
        elif self.state[1] == self.state[4] == self.state[7] != 0:
            return True
        elif self.state[2] == self.state[5] == self.state[8] != 0:
            return True
        elif self.state[0] == self.state[4] == self.state[8] != 0:
            return True
        elif self.state[2] == self.state[4] == self.state[6] != 0:
            return True
        else:
            print("Next Player ")
            return False

    def print_board(self):
        print(self.sign_to_printable(self.state[0]) + "|" + self.sign_to_printable(self.state[1]) + "|" + self.sign_to_printable(self.state[ 2]))
        print(self.sign_to_printable(self.state[3]) + "|" + self.sign_to_printable(self.state[4]) + "|" + self.sign_to_printable(self.state[ 5]))
        print(self.sign_to_printable(self.state[6]) + "|" + self.sign_to_printable(self.state[7]) + "|" + self.sign_to_printable(self.state[ 8]))
            
    def makeMove(self, cell):
        if self.is_valid_turn(cell):
            self.state[cell] = self.activePlayer.symbol
            return True
        return False
    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False
    def getActivePlayerName(self):
        return self.activePlayer.name
class Player:
    def __init__(self, symbol):
        self.name = input("What is your name?")
        self.symbol = symbol
        print("Welcome " + self.name + ". ")
if __name__ == '__main__':
    board = Board()
    symbol_x = 1
    symbol_o = 2
    playerOne = Player(symbol_x)
    playerTwo = Player(symbol_o)
    board.players = [playerOne, playerTwo]
    print("Let's start the game!")
    while not board.is_board_full():
        board.print_board()
        board.changeActivePlayer()
        try:
            cell = int(input("Make your move " + board.getActivePlayerName() + "! Where do you want to make your sign [1-9]: "))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Please enter a number between 1 and 9: ")
            continue
        if not board.makeMove(cell):
            print("ilegal move, choose a number between 1 and 9: ")
            continue
        if board.checkWin():
            print("You wonn, " + board.getActivePlayerName() + "! GW.")
            break

    

    




