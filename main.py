from flask import Flask, Response, request, jsonify, make_response
import mysql.connector
import json

con = mysql.connector.connect(host='localhost',database='dbagenda1',user='root',password='') 

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)

app = Flask(__name__)



@app.route("/contatos", methods=["GET"])
def seleciona_contatos():
    my_cursor = con.cursor()
    my_cursor.execute('SELECT * FROM contatos')
    meus_contatos = my_cursor.fetchall()

    print(meus_contatos)

    contatos = list()
    for contato in meus_contatos:
        contatos.append(
            {
                'id':contato[0],
                'nome':contato[1],
                'fone':contato[2],
                'e-mail':contato[3]
            }
        )

    return make_response(
        jsonify(mensagem = 'Lista de Contatos', dados = contatos
        )
    )

@app.route("/contatos", methods=['POST'])
def criar_contato():
    contatos = request.json

    my_cursor = con.cursor()
    
    sql = f"INSERT INTO contatos (nome,fone,email) VALUES ('{contatos['nome']}','{contatos['fone']}','{contatos['e-mail']}')"

    my_cursor.execute(sql)
    con.commit()


    return make_response(jsonify(mensagem = 'Contato cadastrado com sucesso'), dados = contatos
    )

@app.route("/contatos", methods=['DELETE'])
def deletar_contato():
    contatos = request.json
    my_cursor = con.cursor()

    sql = f'DELETE FROM contatos WHERE idcon = {""}'

    my_cursor.execute(sql)
    con.commit()


    return make_response(jsonify(mensagem = 'Contato deletado com sucesso'), dados = contatos
    )


app.run()
