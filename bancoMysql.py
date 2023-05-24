import mysql.connector

#Projeto particular meu que já existia no mysql db_Agenda1

con = mysql.connector.connect(host='localhost',database='dbagenda1',user='root',password='')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")