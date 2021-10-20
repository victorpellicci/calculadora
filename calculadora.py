import tkinter as tk
import sys
import pygubu


#1: Create a builder
builder = pygubu.Builder()

#2: Load an ui file
builder.add_from_file('calculadora.ui')


class CalculadoraApp:

    def __init__(self):

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')
        self.entry1 = builder.get_object('entry1')
        self.entry2 = builder.get_object('entry2')
        self.entry3 = builder.get_object('entry3')


    def run(self):
        self.mainwindow.mainloop()

    def adicao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,float(caixa1)+float(caixa2))

    def subtracao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,float(caixa1)-float(caixa2))

    def multiplicacao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,float(caixa1)*float(caixa2))

    def divisao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        def texto_erro(): 
            if (caixa2==0):
                print('Erro! Divisão por zero!')
            else:   
                print(float(caixa1)/float(caixa2))
        self.entry3.insert(0,texto_erro)

    def potenciacao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,float(caixa1)**float(caixa2))

    def radiciacao(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,float(caixa1)**(1/float(caixa2)))

if __name__ == '__main__':



    app = CalculadoraApp()
    builder.connect_callbacks(CalculadoraApp())
    app.run()