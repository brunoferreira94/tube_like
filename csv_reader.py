import mysql.connector as conectar
from mysql.connector import errorcode

try:
    conexao = conectar.connect(user='root', password='Kurosaki1', host='127.0.0.1', database='tube_like')
    cursor = conexao.cursor()
    add_video = "INSERT INTO "
    with open('/home/bruno/Downloads/tube8_tmpEmbedDump.csv') as arquivo:
        for linha in arquivo:
            itens = linha.split('|')
            for item in itens:
                print(item)
            break

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    conexao.close()



with open('/home/bruno/Downloads/tube8_webmaster.csv') as arquivo:
    for linha in arquivo:
        itens = linha.split('|')
        for item in itens:
            print(item)
        break