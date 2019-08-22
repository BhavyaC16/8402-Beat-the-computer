class my_game_ctrl(object):
    def get_status(self):
        return ["ended", "won", "running"]

    def get_board(self):
        board = [[0, 0, 0, 0],
                 [0, 0, 0, 2],
                 [0, 0, 0, 2],
                 [0, 0, 0, 4]]
        return board

    def get_score(self):
        return 4

    def execute_move(self, move):
        move = [0, 2, 3, 1][move]

    
        
