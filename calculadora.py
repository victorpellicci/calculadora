import tkinter as tk
import sys
import pygubu

class CalculadoraApp:

    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('calculadora.ui')

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')

    def run(self):
        self.mainwindow.mainloop()

    def adicao(self):
        print("fef")

    def subtracao(self):
        print("sgnsngrgrs")

if __name__ == '__main__':
    app = CalculadoraApp()
    app.run()