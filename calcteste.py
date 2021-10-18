import tkinter as tk
import sys
import pygubu
 
 
class CalculadoraApp(object):
     
    def __init__(self, **kw):
        #insira toda a inicialização aqui
        self.root = tk.Tk()
        
                            
        #1: Crie um buider
        self.builder = builder = pygubu.Builder()
        #2: leia o arquivo  ui .
        builder.add_from_file('calculadora.ui')       
         
        #3: Create a janela principal
        self.mainwindow = builder.get_object('mainwindow', self.root)
        self.mainwindow.title("Calculadora exemplo")
 
 
    def execute(self):
        self.root.mainloop()
 
    def adicao(self):
        print("fef")
        button1.config(text='Fui clicado!')
        label1.config(text='O botão foi apertado')
        button2.config(text='O do lado foi clicado')

    def subtracao(self):
        print("sgnsngrgrs")
 
def main(args):
    app_proc = CalculadoraApp()
    app_proc.execute()
    return 0
 
     
    return 0
 
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))