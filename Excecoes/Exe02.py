'''
2- Dada a lista de frutas: frutas = ["Maçã", "Banana", "Laranja", "Uva"].
Escreva um programa que peça ao usuário para digitar um índice de 0 a 3 para escolher uma fruta. 
Trate adequadamente:
 - ValueError, caso o usuário digite texto ou símbolos em vez de um número inteiro.
 - IndexError, caso o usuário digite um índice que não existe na lista.
 - Ao final, use um bloco finally para exibir a mensagem: "Consulta de frutas finalizada.".
'''

frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']

def busca_fruta(index):
    fruta = frutas[index]
    print(f'Fruta encontrada: {fruta}')

while True:
    try:
        indice = int(input('Informe o indice para a lista: '))
        busca_fruta(indice)
        break
    except ValueError:
        print('O valor deve ser um numero inteiro!')
    except IndexError:
        print('O valor esta fora da area da lista [0-3]')
    finally:
        print('Consulta de frutas finalizada.')