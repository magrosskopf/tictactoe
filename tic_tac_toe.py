
class Board:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.players = []
        self.active_player = ""
    def is_board_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True
    def change_active_player(self):
        if self.active_player == self.players[0]:
            self.active_player = self.players[1]
        else:
            self.active_player = self.players[0]
    def sign_to_printable(self, sign):
        signs = {
            0: " ",
            1: "X",
            2: "O"
        }
        return signs[sign]

    def check_win(self):
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
            print("Next Player")
            return False

    def print_board(self):
        print(self.sign_to_printable(self.state[0]) + "|"
            + self.sign_to_printable(self.state[1]) + "|"
            + self.sign_to_printable(self.state[ 2]))
        print(self.sign_to_printable(self.state[3]) + "|"
            + self.sign_to_printable(self.state[4]) + "|"
            + self.sign_to_printable(self.state[ 5]))
        print(self.sign_to_printable(self.state[6]) + "|"
            + self.sign_to_printable(self.state[7]) + "|"
            + self.sign_to_printable(self.state[ 8]))
        
    def make_move(self, cell):
        if self.is_valid_turn(cell):
            self.state[cell] = self.active_player.symbol
            return True
        return False
    def is_valid_turn(self, cell):
        if self.state[cell] == 0:
            return True
        else:
            return False
    def get_active_playername(self):
        return self.active_player.name
class Player:
    def __init__(self, symbol):
        self.name = input("What is your name?")
        self.symbol = symbol
        print("Welcome " + self.name + ". ")
if __name__ == '__main__':
    board = Board()
    SYMBOL_X = 1
    SYMBOL_O = 2
    player_one = Player(SYMBOL_X)
    player_two = Player(SYMBOL_O)
    board.players = [player_one, player_two]
    print("Let's start the game!")
    while not board.is_board_full():
        board.print_board()
        board.change_active_player()
        try:
            cell = int(input("Make your move " + board.get_active_playername() + 
            "! Where do you want to make your sign [1-9]: "))
        except ValueError:
            continue
        cell = cell - 1
        if cell < 0 or cell > 8:
            print("Please enter a number between 1 and 9: ")
            continue
        if not board.make_move(cell):
            print("ilegal move, choose a number between 1 and 9: ")
            continue
        if board.check_win():
            print("You wonn, " + board.get_active_playername() + "! GW.")
            break