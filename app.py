
from flask import Flask, render_template,request,redirect,session
import mysql
import mysql.connector
from model.musica import recuperar_musicas
from model.musica import adicionar_musica
from model.musica import deletar_musica
from model.musica import alterar_musica

from model.usuario_model import adicionar_usuario
from model.usuario_model import autenticar_usuario

from model.genero import recuperar_generos

app = Flask(__name__)

app.secret_key='chave-secreta-demais'

@app.route("/")
@app.route("/home",methods=["GET"])
def pag_principal():
    musicas = recuperar_musicas(1)
    genero = recuperar_generos()

    return render_template("principal.html",musicas=musicas,genero=genero)

@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/login/post",methods=["POST"])
def pag_login_post():

    login= request.form.get("login")
    senha= request.form.get("senha")

    if autenticar_usuario(login,senha):
        session['usuario_logado'] = login
        return redirect("/admin")
    else:
        return redirect("/login")


@app.route("/cadastro")
def pag_cadastro():
    return render_template("cadastro.html")



@app.route("/cadastro/post",methods=["POST"])
def pag_cadastro_post():
    login = request.form.get("login_create")
    senha = request.form.get("senha_create")
    adicionar_usuario(login,senha)

    return redirect("/login")



@app.route("/admin")
def pag_adm():
    musicas = recuperar_musicas(0)
    genero = recuperar_generos()
    if 'usuario_logado' in session:
        return render_template("administracao.html",musicas=musicas,genero=genero)
    else:
        return redirect("/login")


@app.route("/admin",methods=["POST"])
def pag_adm_post():
    musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url_capa = request.form.get("url_capa")
    genero= request.form.get("nome_genero")

    
    adicionar_musica(cantor,duracao,musica,url_capa,genero)
    return redirect("/admin")

@app.route("/admin/delete/<int:id>")
def deletar(id):
    deletar_musica(id)
    return redirect("/admin")
    
@app.route("/admin/alterar/<int:id>")
def alterar(id):
    alterar_musica(id)
    return redirect("/admin")
    
@app.route("/filtrar/<genero_musica>")
def filtro(genero_musica):
    genero = recuperar_generos()
    musicas = recuperar_musicas(1,genero_musica)

    return render_template("principal.html",musicas=musicas,genero=genero)

@app.route("/logout")
def clear_session():
    session.clear()
    return redirect("/login")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)


