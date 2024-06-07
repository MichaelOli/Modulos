#Importando o modulo
from modulo import *
import time
#programa principal

if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção Desejada: ')
        match opcao:
            case '1':
                b = int(input('Base do quadrilatero:'))
                h = int(input('Altura do quadrilatero:'))
                print(f'Área do quadrlátero: {calcular_quadrilatero(b,h)}')
                continue
            case '2':
                r = int(input('Raio do cículo: '))
                print(f'Área do cículo: {calcular_circulo(r)}.')
                continue
            case '3':
                b = int(input('Área do Triangulo: '))
                h = int(input('Altura do Triangulo: '))
                print(f'Área do Triangulo: {calcular_triagulo(b,h)}')
                continue
            case '4':
                b_menor = int(input('Base menor: '))
                b_maior = int(input('Base maior: '))
                h = int(input('Altura do trapezio: '))
                print(f'Area do trapezio: {calcular_trapezio(b_menor, b_maior, h)}')
            case '5':
                print("Saindo do programa...")
                break
