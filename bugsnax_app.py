import requests
from draw_alpha_with_turtle import *
import tkinter as tk
import turtle

url = "https://www.bugsnaxapi.com/api"


class BugsnaxFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.list_of_bugs = get_bugsnax()
        # self.text_box = tk.Text(self)

        for i in range(len(self.list_of_bugs)):
            name = self.list_of_bugs[i]['name']
            row = i % 24
            col = 0
            if 24 <= i < 48:
                col = 1
            elif 48 <= i < 72:
                col = 2
            elif 72 <= i < 96:
                col = 3
            elif i >= 96:
                col = 4

            tk.Button(self, text=name, command=lambda bug_name=name:
            self.draw_name(bug_name)).grid(row=row, column=col)

    def draw_name(self, name: str):
        DrawAlpha.draw_word(name)
        done()


def get_bugsnax():
    response = requests.get(url + '/bugsnax')
    res = response.json()
    return res['bugsnax']


def get_location():
    response = requests.get(url + '/locations')
    res = response.json()
    return res['locations']


def get_grumpus():
    response = requests.get(url + '/grumpuses')
    res = response.json()
    return res['grumpuses']


bugsnax_dict = get_bugsnax()
location_dict = get_location()
grumpus_dict = get_grumpus()

root = tk.Tk()
f = BugsnaxFrame(root)
f.pack()
root.mainloop()
