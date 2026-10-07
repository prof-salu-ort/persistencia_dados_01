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

def inserir_aluno(conexao, nome, curso):
    sql = 'INSERT INTO alunos (nome, curso) VALUES (%s, %s)'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, curso))
            conexao.commit()
            print(f'Aluno cadastrado com sucesso!')
    except Error as e:
        print(f'Error: {e}')


def apagar_aluno(conexao, matricula):
    sql = 'DELETE FROM alunos WHERE matricula = %s'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (matricula,))
            conexao.commit()

            #rowcount --> retorna a quantidade de linhas que foram afetadas no banco de dados
            if cursor.rowcount > 0:
                print(f'Aluno apagado com sucesso!')
            else:
                print(f'Nenhum aluno encontrado.')            
    except Error as e:
        print(f'Error: {e}')
        

def editar_aluno(conexao, nome, curso, matricula):
    sql = 'UPDATE alunos SET nome = %s, curso = %s WHERE matricula = %s'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (nome, curso, matricula))
            conexao.commit()
        #rowcount --> retorna a quantidade de linhas que foram afetadas no banco de dados
            if cursor.rowcount > 0:
                print(f'Aluno alterado com sucesso!')
            else:
                print(f'Nenhum aluno encontrado.') 
    except Error as e:
        print(f'Error: {e}')


def listar_alunos(conexao):
    sql = 'SELECT * FROM alunos'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            #Converte o resultado do banco de dados em uma lista
            registros= cursor.fetchall()
            return registros
    except Error as e:
        print(f'Error: {e}')
        return []


def buscar_aluno_curso(conexao, curso):
    sql = 'SELECT * FROM alunos WHERE curso = %s'
    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (curso,))
            #Converte o resultado do banco de dados em uma lista
            registros= cursor.fetchall()
            return registros
    except Error as e:
        print(f'Error: {e}')
        return []


########Testes#########
conexao = conectar()
print('Conectado ao banco')
#inserir_aluno(conexao, 'Juca Pereira', 'INFORMATICA')
#inserir_aluno(conexao, 'Marcelo', 'INFORMATICA')
#inserir_aluno(conexao, 'Pedro', 'INFORMATICA')
#inserir_aluno(conexao, 'Ana', 'INFORMATICA')
#inserir_aluno(conexao, 'Enrico', 'INFORMATICA')
#inserir_aluno(conexao, 'Joao', 'INFORMATICA')
#inserir_aluno(conexao, 'Maria Eduarda', 'INFORMATICA')
#inserir_aluno(conexao, 'Bernardo', 'INFORMATICA')
#inserir_aluno(conexao, 'Miguel', 'INFORMATICA')
#inserir_aluno(conexao, 'Sofia', 'ELETRONICA')
#inserir_aluno(conexao, 'Simon', 'MULTIMIDIA')
#apagar_aluno(conexao, 6)
#editar_aluno(conexao, 'Juca Pereira', 'Analise de sistemas', 7)

lista = buscar_aluno_curso(conexao, 'INFORMATICA')

if lista:
    for x in lista:
        print(f'Matricula: {x[0]:03d} | Nome: {x[1]} | Curso: {x[2]}')
else:
    print('Nenhum aluno encontrado')

conexao.close()