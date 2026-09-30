'''
1- Crie um programa que solicite ao usuário uma temperatura em graus Celsius (como texto) e tente convertê-la para 
número decimal (float). Se o usuário digitar algo inválido, trate a exceção ValueError exibindo uma mensagem amigável. 
Caso a conversão ocorra com sucesso, exiba a temperatura convertida para Fahrenheit usando a fórmula: 
F = C * 1.8 + 32 
utilizando a estrutura else.

'''

def converte_temperatura():
    try:
        temp = float(input('Informe a temperatura em Celsius: '))
    except ValueError:
        print('O valor deve ser numérico.')
    else:
        temp_f = (temp * 1.8) + 32    
        print(f'Valor em Fahrenheit: {temp_f}')

converte_temperatura()
