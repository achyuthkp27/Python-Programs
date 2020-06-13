# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 07:01:33 2020

@author: Achyuth
"""

from turtle import Turtle, Screen

CURSOR_SIZE = 20
SQUARE_SIZE = 50
FONT_SIZE = 40
FONT = ('Arial', FONT_SIZE, 'bold')

class TicTacToe:
    def __init__(self):
        self.board = [['?'] * 3 for i in range(3)] # so you can interrogate squares later
        self.turn = 'X'

    def drawBoard(self):
        background = Turtle('square')
        background.shapesize(SQUARE_SIZE * 3 / CURSOR_SIZE)
        background.color('black')
        background.stamp()
        background.hideturtle()

        for j in range(3):
            for i in range(3):
                box = Turtle('square', visible=False)
                box.shapesize(SQUARE_SIZE / CURSOR_SIZE)
                box.color('white')
                box.penup()
                box.goto(i * (SQUARE_SIZE + 2) - (SQUARE_SIZE + 2), j * (SQUARE_SIZE + 2) - (SQUARE_SIZE + 2))
                box.showturtle()
                box.stamp()  # blank out background behind turtle (for later)

                self.board[j][i] = box
                box.onclick(lambda x, y, box=box, i=i, j=j: self.mouse(box, i, j))

    def mouse(self, box, i, j):
        box.onclick(None)  # disable further moves on this square

        # replace square/turtle with (written) X or O
        box.hideturtle()
        box.color('black')
        box.sety(box.ycor() - FONT_SIZE / 2)
        box.write(self.turn, align='center', font=FONT)

        self.board[j][i] = self.turn  # record move

        self.turn = ['X', 'O'][self.turn == 'X']  # switch turns

screen = Screen()

game = TicTacToe()

game.drawBoard()

screen.mainloop()