'''
3- Crie uma função chamada cadastrar_nota(nota). A função deve aceitar valores entre 0 e 10. 
Caso a nota seja menor que 0 ou maior que 10, lance uma exceção ValueError usando a 
palavra-chave raise com a mensagem "A nota deve estar entre 0 e 10.". 
Em seguida, faça uma chamada dentro de um bloco try...except para capturar a exceção e exibir 
a mensagem de erro.
'''


def cadastrar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError('A nota deve ser um numero e estar entre 0 e 10.')
    print('Nota cadastrada com sucesso!')

try:
    nota = float(input('Informe a nota: '))
    cadastrar_nota(nota)
except ValueError as e:
    print(f'Erro: {e}')