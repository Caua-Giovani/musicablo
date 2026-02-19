
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
    
    cursor.execute("""SELECT musica.id_musica,musica.cantor,musica.duracao,musica.nome,musica.url_capa,musica.nome_genero,genero.cor FROM musica
                        inner join genero on musica.nome_genero = genero.genero ;""")

    musicas=cursor.fetchall()

    cursor.execute("SELECT genero,icone,cor FROM genero;")
    
    genero=cursor.fetchall()

    conexao.close

    return render_template("principal.html",musicas=musicas,genero=genero)

@app.route("/admin")

def pag_adm():
    conexao=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="Musicablo"
    )

    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("""SELECT id_musica,cantor,duracao,nome,url_capa,nome_generoFROM musica;""")

    musicas=cursor.fetchall()

    conexao.close
    return render_template("administracao.html",musicas=musicas)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
