from tkinter import *
 
tela = Tk() #instancia a classe 'Tk()' através da variável 'tela'
tela.title("TELA INICIAL")
tela["bg"] = "light yellow"
tela.geometry("200x200") #define o tamanho da tela em width (largura) x height (altura)
 
Container = Frame() #definimos o container com um frame
Container["pady"] = 10 #posiciona o container na tela a partir do top e bottom
Container["bg"] = "light yellow" # define uma cor de fundo
Container.pack() #para exibir os widgets do container
 
texto = Text(Container)
texto["height"] = 1
texto["width"] = 15
texto.pack()
 
btOK = Button(Container)
btOK["text"] = "OK"
btOK["font"] = ("Calibri", "10","bold")
btOK["width"] = 12
btOK["bg"] = "blue"
btOK.pack()
 
btsair = Button()
btsair["text"] = "SAIR"
btsair["font"] = ("Calibri", "10","bold")
btsair["width"] = 5
btsair["command"] = quit
btsair.pack()
 
tela.mainloop()
