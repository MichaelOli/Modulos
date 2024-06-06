# Importando Briblioteca

from modulo import calcular_circulo

#Entrada de dados
#b= int(input('Informe o valor da base: '))
#h = int(input('Informe o valor da altura: '))

#print(f'Area do quadrilatero: {modulo.calcular_quadrilatero(b,h)}')

r= str(input('Informe o valor do Raio: ')).replace(',','.')

r= float(r)

print(f'Area do circulo: {calcular_circulo(r)}.')