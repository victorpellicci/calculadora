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
        self.dado = "asdfg"
        data = '123455'
        print(data)

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

    def texto_erro(self): 
        caixa1 = self.entry1.get()
        caixa2 = self.entry2.get()
        if (caixa2==0):
            return('Erro! Divisão por zero!')
        else:   
            return(float(caixa1)/float(caixa2))
            
    def divisao(self):
        resultado = self.texto_erro()

        self.entry3.delete(0, 'end')
        self.entry3.insert(0, resultado)

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
        self.label4.config(text='1º numero: Radicando')
        self.label5.config(text='2º numero: Indice')

if __name__ == '__main__':



    app = CalculadoraApp()
    print(app.dado)
    #print(app.data)

    builder.connect_callbacks(CalculadoraApp())
    app.run()