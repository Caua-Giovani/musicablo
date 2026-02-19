from database.conexao import conectar

def recuperar_musicas():
    conexao,cursor = conectar()

     
    cursor.execute("""SELECT musica.id_musica,musica.cantor,musica.duracao,musica.nome,musica.url_capa,musica.nome_genero,genero.cor FROM musica
                        inner join genero on musica.nome_genero = genero.genero ;""")

    musicas=cursor.fetchall()



    conexao.close

    return musicas

