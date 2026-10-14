#No terminal, instalar o drive do postgres
# pip install psycopg2-binary

#Importando as bibliotecas
import psycopg2
from psycopg2 import Error

def conectar():
    try:
        #Conectando no banco de dados
        conexao = psycopg2.connect(
            host= 'localhost',
            database='escola',
            user='postgres',
            password='123456')
        return conexao
    except Error as e:
        print(f'Error: {e}')
        return None

def inserir_cliente(conexao, nome):
    sql = 'INSERT INTO cliente (nome) VALUES (%s) RETURNING id'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, ))
            conexao.commit()
            print(f'Cliente cadastrado com sucesso!')
            
            #Ultimo id criado
            ultimo_id = cursor.fetchone()[0]            
            return ultimo_id
    except Error as e:
        print(f'Error: {e}')

def inserir_carro(conexao, placa, id_cliente):
    sql = 'INSERT INTO carro (placa, id_cliente) VALUES (%s, %s)'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (placa, id_cliente))
            conexao.commit()
            print(f'Carro cadastrado com sucesso!')
    except Error as e:
        print(f'Error: {e}')



########Testes#########
conexao = conectar()
print('Conectado ao banco')

id_do_cliente = inserir_cliente(conexao, 'Ana')
inserir_carro(conexao, 'xyz9876', id_do_cliente)

conexao.close()