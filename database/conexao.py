import mysql.connector
class Conectar():

    def conecatar(self):
        
        conexao=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="Musicablo"
            )
        
        cursor=conexao.cursor(dictionary=True)

        return conexao, cursor
