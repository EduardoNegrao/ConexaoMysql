import pymysql
def perguntar():
    resposta = input("O que deseja realizar?\n"+
                     "<I> - Para inserir dados na tabela\n"+
                     "<S> - Para selecionar dados na tabela\n"+
                     "<U> - Para atualizar dados na tabela\n"+
                     "<D> - Para deletar dados na tabela\n"+
                     "<SAIR> - Para finalizar\n").upper()
    return resposta
def insert():
    conn = pymysql.connect(host='127.0.0.1', port=3306, database='provaparcial', user='root', password='root')
    cursor = conn.cursor()

    tabela = input("Informe em qual tabela deseja inserir - Post (P) ou Comment (C)\n").upper()
    if tabela == 'P':
        titulo = input("Informe o titulo do post")
        data = input("Informe a data de criação do post (aaaa/mm/dd)")
        texto = input("Informe a descriçao do post")

        cursor.execute("INSERT INTO post (titlePost,createdPost, textPost) VALUES (%s,%s,%s)", (titulo, data, texto))
        conn.commit()
        print('Post criado')
    if tabela == 'C':
        text = input("Comentário: ")
        user = input("Usuário: ")
        date = input("Informe a data do comentário (aaaa/mm/dd)")
        postId = int(input("Informe o id do post: "))
        cursor.execute("INSERT INTO tablecomment (textComment,userComment, createdComment, postId) VALUES (%s,%s,%s,%s)", (text, user, date, postId))
        conn.commit()
        print('Comentário criado')

    conn.close()
def select():
    conn = pymysql.connect(host='127.0.0.1', port=3306, database='provaparcial', user='root', password='root')
    cursor = conn.cursor()
    tabela = input("Informe qual tabela deseja visualizar - Post (P) ou Comment (C)\n").upper()
    if tabela == 'P':
        cursor.execute("SELECT * from post ")
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nenhum post cadastrado")
        for x in resultado:
            print(x)
    if tabela == 'C':
        cursor.execute("SELECT * from tablecomment")
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nenhum comentário cadastrado")
        for x in resultado:
            print(x)

    conn.close()
def update():
    conn = pymysql.connect(host='127.0.0.1', port=3306, database='provaparcial', user='root', password='root')
    cursor = conn.cursor()
    tabela = input("Informe qual tabela deseja atualizar - Post (P) ou Comment (C)\n").upper()
    if tabela == 'P':
        id = int(input("Informe o id do post que deseja atualizar: "))
        titulo = input("Informe o novo titulo do post: ")
        data = input("Informe a data de atualizacao do post (aaaa/mm/dd): ")
        texto = input("Informe a nova descriçao do post: ")
        cursor.execute("UPDATE post SET titlePost = %s,createdPost = %s, textPost = %s where postId = %s", (titulo, data, texto, id))
        conn.commit()
        print('Post atualizado')
    if tabela == 'C':
        id = int(input("Informe o id do comentário que deseja atualizar: "))
        text = input("Novo Comentário: ")
        user = input("Novo Usuário: ")
        date = input("Informe a nova data do comentário (aaaa/mm/dd): ")
        cursor.execute("UPDATE tablecomment SET textComment = %s ,userComment = %s, createdComment = %s where commentId = %s", (text, user, date, id))
        conn.commit()
        print('Comentário atualizado')
    conn.close()
def delete():
    conn = pymysql.connect(host='127.0.0.1', port=3306, database='provaparcial', user='root', password='root')
    cursor = conn.cursor()
    tabela = input("Informe de qual tabela deseja deletar - Post (P) ou Comment (C)\n").upper()
    if tabela == 'P':
        id = int(input("Informe o id do post que deseja remover: "))
        cursor.execute("DELETE FROM post WHERE postId = %s", (id))
        conn.commit()
        print('Post deletado')
    if tabela == 'C':
        id = int(input("Informe o id do comentário que deseja remover: "))
        cursor.execute("DELETE FROM tablecomment WHERE commentId = %s", (id))
        conn.commit()
        print('Comentário deletado')

    conn.close()