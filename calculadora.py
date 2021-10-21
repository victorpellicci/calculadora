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
        self.label4 = builder.get_object('label4')
        self.label5 = builder.get_object('label5')
        self.checkbutton1 = builder.get_object('checkbutton1')
        print(self.checkbutton1.state())
        self.dado = "asdfg"
        data = '123455'
        print(data)

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
        if (self.checkbutton1.state()[0]=='alternate' or self.checkbutton1.state()[0]==''):
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry3.insert(0,self.adicaoerro())

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

    def manter(self):
        print(self.checkbutton1.state())

if __name__ == '__main__':

    app = CalculadoraApp()
    print(app.dado)

    builder.connect_callbacks(CalculadoraApp())
    app.run()