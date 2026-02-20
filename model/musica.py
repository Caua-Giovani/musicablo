from database.conexao import conectar



def recuperar_musicas():
    conexao,cursor = conectar()

     
    cursor.execute("""SELECT musica.id_musica,musica.cantor,musica.duracao,musica.nome,musica.url_capa,musica.nome_genero,genero.cor FROM musica
                        inner join genero on musica.nome_genero = genero.genero 
                        ORDER BY musica.id_musica ASC;""")

    musicas=cursor.fetchall()



    conexao.close()

    return musicas

def adicionar_musica(cantor:str,duracao:str,musica:str,url_capa:str,genero:str) -> bool:
    """
    Adicona músicas com as informações passadas através dos parâmetros.
    """

    conexao,cursor = conectar()

     
    cursor.execute("""INSERT INTO musica (cantor, duracao, nome, url_capa, nome_genero)
                   VALUES(%s,%s,%s,%s,%s)""",(cantor,duracao,musica,url_capa,genero) )

    conexao.commit()
    conexao.close()

