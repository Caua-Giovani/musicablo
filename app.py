from flask import Flask, render_template,request,redirect,session
import mysql
import mysql.connector

app = Flask(__name__)

@app.route("/")
@app.route("/home",methods=["GET"])
def pag_principal():
    conexao=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="Musicablo"
    )

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_musica,cantor,duracao,nome,url_capa,nome_genero FROM musica;")
    musicas=cursor.fetchall()

    return render_template("principal.html",musicas=musicas)

@app.route("/admin")

def pag_adm():
    return render_template("administracao.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)