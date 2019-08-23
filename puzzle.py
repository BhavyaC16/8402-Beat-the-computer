import random
from tkinter import Frame, Label, CENTER
from ai import find_best_move
from our_logic import get_participant_output
import logic
import math
import constants as c
from time import sleep
import sys

class GameGrid(Frame):
    def __init__(self, player_args):
        Frame.__init__(self)
        self.grid()
        self.master.title('8402 - Beat the computer')
        #self.master.bind("<Key>", self.key_down)

        # self.gamelogic = gamelogica
        self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
                         c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right,
                         c.KEY_UP_ALT: logic.up, c.KEY_DOWN_ALT: logic.down,
                         c.KEY_LEFT_ALT: logic.left,
                         c.KEY_RIGHT_ALT: logic.right}

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.player_file = player_args
        self.score = 0
        while(logic.game_state(self.matrix) != 'win' and logic.game_state(self.matrix) != 'lose'):
            self.key_down("<Key>")
        if logic.game_state(self.matrix) == 'win':
            self.grid_cells[1][1].configure(
                text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(
                text="Lose", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[2][1].configure(
                text="Score", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[2][2].configure(
                text=str(self.score), bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        if logic.game_state(self.matrix) == 'lose':
            self.grid_cells[1][1].configure(
                text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[1][2].configure(
                text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[2][1].configure(
                text="Score", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            self.grid_cells[2][2].configure(
                text=str(self.score), bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        sleep(5)
        self.mainloop()
        #self.master.destroy()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def gen(self):
        return random.randint(0, c.GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_two(self.matrix)
        self.matrix = logic.add_two(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number] if new_number <= 65536 else c.BACKGROUND_COLOR_DICT[65536],
                                                    fg=c.CELL_COLOR_DICT[new_number] if new_number <= 65536 else c.CELL_COLOR_DICT[65536])
        self.update_idletasks()

    def check_participant_output_validity(self, part_out, game_board):
        return(True)

    def penalty(game_board):
        return(game_board)

    def key_down(self, event):
        game_board = self.matrix
        move = find_best_move(list(map(lambda x: list(map(lambda y: 0 if y==0 else y.bit_length()-1, x)), game_board)))
        if(move==0):
            move = 'w'
        elif(move==1):
            move = 's'
        elif(move==2):
            move = 'a'
        elif(move==3):
            move = 'd'
        else:
            self.game_over()
        key = repr(move)
        if key in self.commands:
            self.matrix, done, self.score = self.commands[repr(move)](self.matrix, self.score)
            #print("SCORE:")
            #print(self.score)
            if done:
                #self.matrix = logic.add_two(self.matrix)
                # record last move
                part_out = get_participant_output(self.player_file, self.matrix, {'w':'up', 's': 'down', 'a': 'left', 'd': 'right'}[move])
                if self.check_participant_output_validity(part_out, game_board):
                    self.matrix[part_out[0][1]][part_out[0][0]] = part_out[1]
                else:
                    penalty(game_board)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                done = False
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = [2,4,8,16,32][random.randint(0,4)]


eval_args = sys.argv[1].split(' ')
scores=[]

for i in range(4):
    game = GameGrid(eval_args)
    scores.append(game.score)
print(scores)
