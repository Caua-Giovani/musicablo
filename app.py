from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)

@app.route("/")

def pag_principal():
    return render_template("principal.html")

@app.route("/admin")

def pag_adm():
    return render_template("administracao.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)