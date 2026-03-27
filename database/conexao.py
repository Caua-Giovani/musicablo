import mysql.connector

def conectar():
    tipo_conexao = "NUVEM"
    if tipo_conexao == "LOCAL":
        conexao=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="Musicablo"
            )
    else:
        conexao=mysql.connector.connect(
                host="mysql-289071e4-servidor-caua.j.aivencloud.com",
                port=16660,
                user="avnadmin",
                password="AVNS_Q-U2mYvJ-2Fv-uGD6DB",
                database="Musicablo"
            )
    
    cursor=conexao.cursor(dictionary=True)

    return conexao, cursor

