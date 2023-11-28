print('Conversor de Real para Dolar e Euro')
real = float(input('Digite o valor que deseja Converter: R$ '))
dolar = real / 4.91
euro = real / 5.34
print(' Com R$ {:.2f}\n você pode comprar US$ {:.2f} e {:.2f} Euros'.format(real, dolar, euro))

