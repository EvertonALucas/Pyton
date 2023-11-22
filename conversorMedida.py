# Conversor de Medidas Km hm dam m dm cm mm
medida = float(input('Uma distância em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:'.format(medida))
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{} dm'.format(dm))
print('{} cm'.format(cm))
print('{} mm'.format(mm))
