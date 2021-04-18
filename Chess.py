'''
To Do
-Make movement system
  -Mouse click to move pieces
  -Movement check system
  -Winning and losing check
  -

Ideas
-Play against the computer
-Play on two different devices
-Start and End screen
'''

from turtle import Turtle, Screen
import turtle
import numpy


class Piece:
    def __init__(self, color, typ, num):
        self.color = color
        self.typ = typ
        self.num = num


b = Turtle()
p = Turtle()
b.ht()
p.ht()
bp1 = Piece("black", "pawn", 1)
bp2 = Piece("black", "pawn", 2)
bp3 = Piece("black", "pawn", 3)
bp4 = Piece("black", "pawn", 4)
bp5 = Piece("black", "pawn", 5)
bp6 = Piece("black", "pawn", 6)
bp7 = Piece("black", "pawn", 7)
bp8 = Piece("black", "pawn", 8)
br1 = Piece("black", "rook", 1)
br2 = Piece("black", "rook", 2)
bn1 = Piece("black", "knight", 1)
bn2 = Piece("black", "knight", 2)
bb1 = Piece("black", "bishop", 1)
bb2 = Piece("black", "bishop", 2)
bk1 = Piece("black", "king", 1)
bq1 = Piece("black", "queen", 1)

wp1 = Piece("white", "pawn", 1)
wp2 = Piece("white", "pawn", 2)
wp3 = Piece("white", "pawn", 3)
wp4 = Piece("white", "pawn", 4)
wp5 = Piece("white", "pawn", 5)
wp6 = Piece("white", "pawn", 6)
wp7 = Piece("white", "pawn", 7)
wp8 = Piece("white", "pawn", 8)
wr1 = Piece("white", "rook", 1)
wr2 = Piece("white", "rook", 2)
wn1 = Piece("white", "knight", 1)
wn2 = Piece("white", "knight", 2)
wb1 = Piece("white", "bishop", 1)
wb2 = Piece("white", "bishop", 2)
wk1 = Piece("white", "king", 1)
wq1 = Piece("white", "queen", 1)

s = Screen()

b.ht()
s.tracer(0, 0)
s.bgcolor("blue")

pieces = [[0 for i in range(8)] for j in range(8)]
i1 = -1
j1 = -1
turn = 1


def square(x, y, c):
    b.penup()
    b.goto(x, y)
    b.pendown()
    b.setheading(0)
    b.fillcolor(c)
    b.begin_fill()
    for i in range(4):
        b.forward(80)
        b.right(90)
    b.end_fill()


def board():
    b.penup()
    b.goto(-320, 320)
    b.pendown()
    x = -320
    y = 320
    color = "#856840"
    for i in range(8):
        for j in range(8):
            square(x, y, color)
            if color == "#856840":
                color = "#ffae3d"
            else:
                color = "#856840"
            x += 80
        if color == "#856840":
            color = "#ffae3d"
        else:
            color = "#856840"
        x = -320
        y -= 80


def setup():
    board()
    pieces[0][0] = wr1
    pieces[0][1] = wn1
    pieces[0][2] = wb1
    pieces[0][3] = wk1
    pieces[0][4] = wq1
    pieces[0][5] = wb2
    pieces[0][6] = wn2
    pieces[0][7] = wr2
    pieces[1][0] = wp1
    pieces[1][1] = wp2
    pieces[1][2] = wp3
    pieces[1][3] = wp4
    pieces[1][4] = wp5
    pieces[1][5] = wp6
    pieces[1][6] = wp7
    pieces[1][7] = wp8

    pieces[7][0] = br1
    pieces[7][1] = bn1
    pieces[7][2] = bb1
    pieces[7][3] = bk1
    pieces[7][4] = bq1
    pieces[7][5] = bb2
    pieces[7][6] = bn2
    pieces[7][7] = br2
    pieces[6][0] = bp1
    pieces[6][1] = bp2
    pieces[6][2] = bp3
    pieces[6][3] = bp4
    pieces[6][4] = bp5
    pieces[6][5] = bp6
    pieces[6][6] = bp7
    pieces[6][7] = bp8
    print("It is white's move.")


def translation():
    board()
    for i in range(8):
        for j in range(8):
            if pieces[i][j] != 0:
                if (pieces[i][j]).typ == "pawn":
                    pawn(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)
                if (pieces[i][j]).typ == "rook":
                    rook(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)
                if (pieces[i][j]).typ == "knight":
                    knight(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)
                if (pieces[i][j]).typ == "bishop":
                    bishop(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)
                if (pieces[i][j]).typ == "queen":
                    queen(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)
                if (pieces[i][j]).typ == "king":
                    king(-280 + 80 * j, -320 + 80 * i, pieces[i][j].color)


def pawn(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.seth(0)
    p.circle(24, 45)
    p.circle(40, 90)
    p.circle(24, 90)
    p.circle(40, 90)
    p.circle(24, 45)
    p.end_fill()


def rook(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.seth(0)
    p.forward(30)
    p.left(90)
    p.forward(72)
    p.left(90)
    p.forward(60)
    p.left(90)
    p.forward(72)
    p.left(90)
    p.forward(30)
    p.end_fill()


def knight(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.seth(90)
    p.forward(42)
    p.right(60)
    p.forward(30)
    p.left(120)
    p.forward(30)
    p.left(30)
    p.forward(30)
    p.left(90)
    p.forward(72)
    p.left(90)
    p.forward(30)
    p.end_fill()


def bishop(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.setheading(0)
    p.forward(15)
    p.left(102)
    p.forward(73.5)
    p.left(156)
    p.forward(73.5)
    p.setheading(0)
    p.forward(15)
    p.end_fill()


def queen(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.seth(0)
    p.forward(20)
    p.left(117)
    p.forward(45)
    p.seth(0)
    p.circle(16)
    p.seth(243)
    p.forward(45)
    p.seth(0)
    p.forward(20)
    p.end_fill()


def king(x, y, c):
    p.pencolor(c)
    p.fillcolor(c)
    p.pu()
    p.goto(x, y)
    p.pd()
    p.begin_fill()
    p.seth(0)
    p.forward(20)
    p.left(90)
    p.forward(40)
    p.left(90)
    p.forward(20)
    p.seth(0)
    p.circle(16)
    p.seth(180)
    p.forward(20)
    p.left(90)
    p.forward(40)
    p.left(90)
    p.forward(20)
    p.end_fill()


def click(x, y):
    global i1, j1
    if i1 == -1 and pieces[int(y / 80 + 4)][int(x / 80 + 4)] != 0:
        i1 = int(y / 80 + 4)
        j1 = int(x / 80 + 4)
    else:
        move(i1, j1, int(y / 80 + 4), int(x / 80 + 4))


def move(i_1, j_1, i_2, j_2):
    global i1, j1, turn
    if pieces[i_1][j_1] != 0:
        valid = True
        if pieces[i_2][j_2] != 0 and pieces[i_2][j_2].color == pieces[i_1][j_1].color:
            valid = False
        elif pieces[i_1][j_1].typ == "pawn":
            if pieces[i_1][j_1].color == "black":
                if (i_2 == i_1 - 1 or i_1 == 6 and i_2 == 4) and j_2 == j_1 and pieces[i_2][j_2] == 0:
                    valid = True
                    if i_2 == 0:
                        pieces[i_1][j_1].typ = "queen"
                elif i_2 == i_1 - 1 and (j_2 == j_1 + 1 or j_2 == j_1 - 1) and pieces[i_2][j_2] != 0 and pieces[i_2][j_2].color == "white":
                    valid = True
                    if i_2 == 0:
                        pieces[i_1][j_1].typ = "queen"
                else:
                    valid = False
            if pieces[i_1][j_1].color == "white":
                if (i_2 == i_1 + 1 or i_1 == 1 and i_2 == 3) and j_2 == j_1 and pieces[i_2][j_2] == 0:
                    valid = True
                    if i_2 == 7:
                        pieces[i_1][j_1].typ = "queen"
                elif i_2 == i_1 + 1 and (j_2 == j_1 + 1 or j_2 == j_1 - 1) and pieces[i_2][j_2] != 0 and pieces[i_2][j_2].color == "black":
                    valid = True
                    if i_2 == 7:
                        pieces[i_1][j_1].typ = "queen"
                else:
                    valid = False
        elif pieces[i_1][j_1].typ == "rook":
            if i_1 == i_2:
                for k in range(1, abs(j_2 - j_1)):
                    if pieces[i_1][j_2-k*numpy.sign(j_2-j_1)] != 0:
                        valid = False
                        break
            elif j_1 == j_2:
                for k in range(1, abs(i_2 - i_1)):
                    if pieces[i_2-k*numpy.sign(i_2-i_1)][j_1] != 0:
                        valid = False
                        break
            else:
                valid = False
        elif pieces[i_1][j_1].typ == "bishop":
            if i_2 - i_1 == j_2 - j_1 or i_2 - i_1 == j_1 - j_2:
                for k in range(1, abs(j_2 - j_1)):
                    if pieces[i_1 + k * numpy.sign(i_2 - i_1)][j_1 + k * numpy.sign(j_2 - j_1)] != 0:
                        valid = False
                        break
            else:
                valid = False
        elif pieces[i_1][j_1].typ == "queen":
            if i_2 - i_1 == j_2 - j_1 or i_2 - i_1 == j_1 - j_2:
                for k in range(1, abs(j_2 - j_1)):
                    if pieces[i_1 + k * numpy.sign(i_2 - i_1)][j_1 + k * numpy.sign(j_2 - j_1)] != 0:
                        valid = False
                        break
            elif i_1 == i_2:
                for k in range(1, abs(j_2 - j_1)):
                    if pieces[i_1][j_2-k*numpy.sign(j_2-j_1)] != 0:
                        valid = False
                        break
            elif j_1 == j_2:
                for k in range(1, abs(i_2 - i_1)):
                    if pieces[i_2-k*numpy.sign(i_2-i_1)][j_1] != 0:
                        valid = False
                        break
            else:
                valid = False
        elif pieces[i_1][j_1].typ == "king":
            if not(((i_2 - i_1 == j_2 - j_1 or i_2 - i_1 == j_1 - j_2) and abs(i_2 - i_1) == 1) or (
                    i_1 == i_2 and abs(j_2-j_1) == 1) or (j_1 == j_2 and abs(i_2-i_1) == 1)):
                valid = False
        elif pieces[i_1][j_1].typ == "knight":
            if abs(i_2 - i_1) == 2 and abs(j_2 - j_1) == 1 or abs(i_2 - i_1) == 1 and abs(j_2 - j_1) == 2:
                valid = True
            else:
                valid = False
        if valid and (pieces[i_1][j_1].color == "black" and turn == 0 or pieces[i_1][j_1].color == "white" and turn
                      == 1):
            pieces[i_2][j_2] = pieces[i_1][j_1]
            pieces[i_1][j_1] = 0
            turn = 1 - turn
            translation()
            if turn == 0:
                print("It is black's move.")
            else:
                print("It is white's move.")
        else:
            print("Invalid move, try again!")
    i1 = -1
    j1 = -1



s.onscreenclick(click)

setup()
translation()
s.update()
turtle.done()
