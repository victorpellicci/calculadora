import tkinter as tk
from tkinter import Tk, Label, Frame, Button
import sys
import pygubu
import time


#1: Create a builder
builder = pygubu.Builder()

#2: Load an ui file
builder.add_from_file('calculadora.ui')

class CalculadoraApp:

    def __init__(self):

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')
        self.mainwindow.master.title("Calculadora VAP")

        self.entry1 = builder.get_object('entry1')
        self.entry2 = builder.get_object('entry2')
        self.entry3 = builder.get_object('entry3')
        self.label4 = builder.get_object('label4')
        self.label5 = builder.get_object('label5')
        self.checkbutton1 = builder.get_object('checkbutton1')
        self.button7 = builder.get_object('button7')

    def run(self):
        self.mainwindow.mainloop()

    def adicaoerro(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)+float(caixa2))
        except ValueError:
            return('Use "." no lugar de ","')

    def adicao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.adicaoerro())
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def subtracaoerro (self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)-float(caixa2))
        except ValueError:
            return('Use "." no lugar de ","')

    def subtracao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.subtracaoerro())
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def multiplicacaoerro (self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)*float(caixa2))
        except ValueError:
            return('Use "." no lugar de ","')

    def multiplicacao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.multiplicacaoerro())
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def divisaoerro(self): 
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)/float(caixa2))
        except ZeroDivisionError:   
            return('Erro! Divisão por zero!')
        except ValueError:
            return('Use "." no lugar de ","')
            
    def divisao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.divisaoerro())
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def potenciacaoerro(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)**float(caixa2))
        except ValueError:
            return('Use "." no lugar de ","')

    def potenciacao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.potenciacaoerro())
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def radiciacaoerro(self):
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        try:
            return(float(caixa1)**(1/float(caixa2)))
        except ValueError:
            return('Use "." no lugar de ","')

    def radiciacao(self):
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.radiciacaoerro())
        self.label4.config(text='1º numero: Radicando')
        self.label5.config(text='2º numero: Indice')
        if ('selected' in self.checkbutton1.state()):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')

    def fechar(self):
        """
        print(self.button7.keys())
        self.button7['text']='Obrigado por usar a calculadora do Victor!'
        
        """
        self.label4.config(text='Obrigado por usar a calculadora do Victor!')
        time.sleep(3)

        #self.mainwindow.master.destroy()
    
if __name__ == '__main__':

    app = CalculadoraApp()
    
    builder.connect_callbacks(CalculadoraApp())

    app.run()