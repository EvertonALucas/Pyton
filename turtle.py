from turtle import *
# movimentando a tartaruga


def quadrado(graus, tamanho):
    for cont in range(4):
        forward(tamanho)
        right(graus)


def triangulo(graus, tamanho):
    for i in ["red", "violet", "orange"]:
        color(i)
        left(graus)
        forward(tamanho)


def touche():
    title("TARTARUGA TOUCHE!")  # coloca o título na janela
    bgcolor("lightyellow")  # coloca a cor de fundo da janela em amarelo claro
    pensize(4)  # define a espessura do traço
    color("blue")  # cor da tartaruga e do traço
    shape("turtle")  # coloca o formato da tartaruga
    delay(50)
    quadrado(90, 200)
    triangulo(120, 150)


touche()         # Chama a função
exitonclick()   # aguarda o clique do mouse para encerrar
