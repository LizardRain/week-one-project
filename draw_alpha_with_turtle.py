from __future__ import annotations
from turtle import *
import tkinter as tk


class DrawAlpha:
    def __init__(self, x_start: float, y_start: float, title: str):
        self.ALPHA_DICT = {
            "A": self.__draw_cap_a, "B": self.__draw_cap_b,
            "C": self.__draw_cap_c, "D": self.__draw_cap_d,
            "E": self.__draw_cap_e, "F": self.__draw_cap_f,
            "G": self.__draw_cap_g, "H": self.__draw_cap_h,
            "I": self.__draw_cap_i, "J": self.__draw_cap_j,
            "K": self.__draw_cap_k, "L": self.__draw_cap_l,
            "M": self.__draw_cap_m, "N": self.__draw_cap_n,
            "O": self.__draw_cap_o, "P": self.__draw_cap_p,
            "Q": self.__draw_cap_q, "R": self.__draw_cap_r,
            "S": self.__draw_cap_s, "T": self.__draw_cap_t,
            "U": self.__draw_cap_u, "V": self.__draw_cap_v,
            "W": self.__draw_cap_w, "X": self.__draw_cap_x,
            "Y": self.__draw_cap_y, "Z": self.__draw_cap_z,
            "a": self.__draw_low_a, "b": self.__draw_low_b,
            "c": self.__draw_low_c, "d": self.__draw_low_d,
            "e": self.__draw_low_e, "f": self.__draw_low_f,
            "g": self.__draw_low_g, "h": self.__draw_low_h,
            "i": self.__draw_low_i, "j": self.__draw_low_j,
            "k": self.__draw_low_k, "l": self.__draw_low_l,
            "m": self.__draw_low_m, "n": self.__draw_low_n,
            "o": self.__draw_low_o, "p": self.__draw_low_p,
            "q": self.__draw_low_q, "r": self.__draw_low_r,
            "s": self.__draw_low_s, "t": self.__draw_low_t,
            "u": self.__draw_low_u, "v": self.__draw_low_v,
            "w": self.__draw_low_w, "x": self.__draw_low_x,
            "y": self.__draw_low_y, "z": self.__draw_low_z,
            " ": self.__draw_space, ".": self.__draw_period,
            "?": self.__draw_question_mark, "!": self.__draw_exclamation_mark,
            "(": self.__draw_open_parenthesis,
            ")": self.__draw_closed_parenthesis}
        self.screen = Screen()
        self.screen.title(title)
        self.screen.clear()
        self.turtle = RawTurtle(self.screen)
        self.turtle.penup()
        self.turtle.setposition(x_start, y_start)
        self.turtle.pendown()

    @classmethod
    def draw_word(cls, word: str, x: float = -750.00, y: float = 00.00):
        draw_alpha = DrawAlpha(x, y, word)

        for letter in word:
            draw_alpha.ALPHA_DICT[letter]()
            if letter != " ":
                draw_alpha.__space_between_letters()

    # non-letter characters
    def __draw_space(self):
        self.turtle.penup()
        self.turtle.sety(0.0)
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.pendown()

    def __space_between_letters(self):
        self.turtle.penup()
        self.turtle.sety(0.0)
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.pendown()

    def __draw_period(self):
        self.turtle.penup()
        self.turtle.sety(-100)
        self.turtle.dot()

    def __draw_question_mark(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(40)
        self.turtle.penup()
        self.turtle.forward(5)
        self.turtle.dot()

        # reset to default
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_exclamation_mark(self):
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.pendown()

        self.turtle.setheading(270)
        self.turtle.forward(95)
        self.turtle.penup()
        self.turtle.forward(5)
        self.turtle.dot()

        # reset to default
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_open_parenthesis(self):
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)
        self.turtle.pendown()
        self.turtle.setheading(180)
        self.turtle.circle(50, 180)

    def __draw_closed_parenthesis(self):
        self.turtle.setheading(0)
        self.turtle.circle(-50, 180)

        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    # capital letters !!
    def __draw_cap_a(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.backward(100)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_b(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(60)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(40)
        self.turtle.right(90)
        self.turtle.forward(40)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 10)

    def __draw_cap_c(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_cap_d(self):
        self.turtle.setheading(0)
        self.turtle.forward(46)
        self.turtle.right(45)
        self.turtle.forward(5)
        self.turtle.right(45)
        self.turtle.forward(92)
        self.turtle.right(45)
        self.turtle.forward(5)
        self.turtle.right(45)
        self.turtle.forward(46)
        self.turtle.right(90)
        self.turtle.forward(100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_e(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_cap_f(self):
        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_g(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(25)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_cap_h(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.backward(100)

    def __draw_cap_i(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(25)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.backward(50)

    def __draw_cap_j(self):
        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(25)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(25)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_k(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.setheading(45)
        self.turtle.setposition(self.turtle.xcor() + 50, 0)
        self.turtle.setposition(self.turtle.xcor() - 50, -50)
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 50, -100)

    def __draw_cap_l(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_cap_m(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(100)

    def __draw_cap_n(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(100)

    def __draw_cap_o(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_p(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_q(self):
        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(100)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.backward(50)
        self.turtle.right(45)
        self.turtle.setposition(self.turtle.xcor() - 25, -75)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_cap_r(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(45)
        self.turtle.setposition(self.turtle.xcor() + 50, -100)

    def __draw_cap_s(self):
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_t(self):
        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(25)
        self.turtle.right(90)
        self.turtle.forward(100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_cap_u(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(100)

    def __draw_cap_v(self):
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 25, -100)
        self.turtle.setheading(45)
        self.turtle.setposition(self.turtle.xcor() + 25, 0)

    def __draw_cap_w(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.backward(100)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(100)

    def __draw_cap_x(self):
        # draw letter
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 50, -100)
        self.turtle.penup()
        self.turtle.sety(0)
        self.turtle.pendown()
        self.turtle.setheading(225)
        self.turtle.setposition(self.turtle.xcor() - 50, -100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_y(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_cap_z(self):
        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.setheading(225)
        self.turtle.setposition(self.turtle.xcor() - 50, -100)
        self.turtle.left(135)
        self.turtle.forward(50)

        # adding the little line in the middle cuz i think its cute
        self.turtle.penup()
        self.turtle.setposition(self.turtle.xcor() - 50, -50)
        self.turtle.pendown()
        self.turtle.forward(50)

    # lowercase letters !!
    def __draw_low_a(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_b(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_c(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_low_d(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_e(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_f(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_g(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(100)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_h(self):
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_i(self):
        # start lower for lower case + funny i things
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.dot()
        self.turtle.pendown()

        # draw letter
        self.turtle.penup()
        self.turtle.sety(-65)
        self.turtle.pendown()
        self.turtle.setheading(270)
        self.turtle.forward(35)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_low_j(self):
        # start lower for lower case + funny j things
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.dot()
        self.turtle.pendown()

        # draw letter
        self.turtle.penup()
        self.turtle.sety(-65)
        self.turtle.pendown()
        self.turtle.setheading(270)
        self.turtle.forward(85)
        self.turtle.right(90)
        self.turtle.forward(25)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_k(self):
        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 50, -100)

    def __draw_low_l(self):
        # funny l things
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)

    def __draw_low_m(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_n(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

    def __draw_low_o(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_p(self):
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_q(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(50)
        self.turtle.backward(100)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_r(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_s(self):
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.right(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_t(self):
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 25)
        self.turtle.pendown()
        self.turtle.setheading(270)
        self.turtle.forward(100)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.backward(50)

    def __draw_low_u(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_low_v(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 25, -100)
        self.turtle.setheading(45)
        self.turtle.setposition(self.turtle.xcor() + 25, -50)

    def __draw_low_w(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(50)
        self.turtle.right(90)
        self.turtle.forward(25)
        self.turtle.left(90)
        self.turtle.forward(50)

    def __draw_low_x(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(315)
        self.turtle.setposition(self.turtle.xcor() + 50, -100)
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()
        self.turtle.setheading(225)
        self.turtle.setposition(self.turtle.xcor() - 50, -100)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_y(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(270)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.left(90)
        self.turtle.forward(50)
        self.turtle.backward(100)
        self.turtle.left(90)
        self.turtle.forward(50)

        # reset to default
        self.turtle.penup()
        self.turtle.setx(self.turtle.xcor() + 50)

    def __draw_low_z(self):
        # start lower for lower case
        self.turtle.penup()
        self.turtle.sety(-50)
        self.turtle.pendown()

        # draw letter
        self.turtle.setheading(0)
        self.turtle.forward(50)
        self.turtle.setheading(225)
        self.turtle.setposition(self.turtle.xcor() - 50, -100)
        self.turtle.left(135)
        self.turtle.forward(50)


'''turt = Turtle()
turt.penup()
turt.setposition(-350, 0.0)
turt.pendown()
DrawAlpha.draw_word(turt, "b(bb)b")
# CAPITAL LETTER TESTING
# word = "THE QUICK BROWN FOX"
# word = "JUMPS OVER THE LAZY"
# word = "DOG"

# LOWERCASE LETTER TESTING
# word = "the quick brown fox"
# word = "jumps over the lazy"
# word = "dog"
done()'''
