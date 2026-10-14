#No terminal, instalar o drive do postgres
# pip install psycopg2-binary

#Importando as bibliotecas
import psycopg2
from psycopg2 import Error


try:
    #Conectando no banco de dados
    conexao = psycopg2.connect(
        host= 'localhost',
        database='escola',
        user='postgres',
        password='123456'
    )

    #Gravando dados no banco
    sql = 'INSERT INTO alunos (nome, curso) VALUES (%s, %s);'
    valores = ('Juca Pereira', 'Informatica')

    #Cursor
    cursor = conexao.cursor()
    ultima_matricula = cursor.fetchone()[0]

    #Ultima matricula criada
    print(ultima_matricula)

    #executando o comando
    cursor.execute(sql, valores)
    conexao.commit()

except Error as e:
    print(f'Erro: {e}')
else:
    print('Conectado ao postgres!!!')
finally:
    conexao.close()
    cursor.close()