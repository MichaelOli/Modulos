from datetime import date

#Função do  quadrilatero
def calcular_quadrilatero(b,h):
    a = b* h
    return a
# Função do  circulo
def calcular_circulo(r):
    a = 3.14*r**2
    return a
# Função do  Triagulo
def calcular_triagulo(b,h):
    a = (b*h)/2
    return a 
# Função do  Trapezio
def calcular_trapezio(b_menor, b_maior,h):
    a = ((b_menor+b_maior)*h)/2
    return a
# Função de Exibir o Menu
def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    print(f'{'='*6} CALCULANDO FIGURAS GEOMETRICAS {'='*6}')
    print(f'\n{dia} de {meses[mes -1]} de {ano}.\n')
   
    print('1 - Calcular quadrilatero')
    print('2 - Calcular Círculo')
    print('3 - Calcular Triângulo')
    print('4 - Calcular Trapezio')
    print('5 - Sair do programa')

