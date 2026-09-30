'''
4- Considere que um cliente possui uma conta com saldo inicial de R$ 500.00. Crie duas funções:
 - depositar(saldo, valor): deve receber o saldo atual e o valor do depósito. 
   Se o valor for menor ou igual a zero, lance uma exceção ValueError com a mensagem 
   "O valor de depósito deve ser positivo.". Caso contrário, retorne o novo saldo. 

 - sacar(saldo, valor): deve receber o saldo atual e o valor do saque. 
   Se o valor for menor ou igual a zero, lance ValueError("O valor do saque deve ser positivo.").
   Se o valor do saque for maior do que o saldo disponível, lance ,
   ValueError("Saldo insuficiente para realizar o saque."). 
   Caso contrário, retorne o saldo atualizado.
'''

def depositar(saldo, valor):
    if valor <= 0:
        raise ValueError('O valor de depósito deve ser positivo.')
    return saldo + valor

def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError('O valor do saque deve ser positivo.')
    if valor > saldo:
        raise ValueError('Saldo insuficiente para realizar o saque.')
    return saldo - valor

'''
Pergunte ao usuário qual operação deseja realizar (1 para Depósito, 2 para Saque).
Peça o valor da transação e execute a operação correspondente dentro de um bloco try...except.

Trate o erro caso o usuário digite um valor não numérico (ValueError do float) e capture também 
as mensagens das regras de negócio disparadas pelo raise.

Use o bloco else para exibir o saldo atualizado em caso de sucesso e o bloco finally para 
informar que o atendimento da operação foi concluído.
'''
saldo = 500
saldo_final = 0

try:
    opcao = int(input('Escolha:\n1- Deposito \n2- Saque\n'))
    valor = float(input('Informe o valor: '))

    if opcao == 1:
        saldo_final = depositar(saldo, valor)
    elif opcao == 2:
        saldo_final = sacar(saldo, valor)

except ValueError as e:
    print(f'Erro: {e}')
else:
    print(f'Saldo final: R${saldo_final:.2f}')
