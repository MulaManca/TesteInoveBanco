from db import conectar_bd, criar_tabelas, inserir_post, listar_posts_bd, atualizar_post_bd, excluir_post as excluir_post_bd, criar_banco_de_dados, inserir_usuario, listar_usuarios_bd, atualizar_usuario, excluir_usuario
from api import listar_posts, criar_post, atualizar_post_api, excluir_post_api, listar_usuarios

def exibir_posts_da_api():
    posts = listar_posts()
    print("Posts da API:")
    for post in posts:
        print(post)

def criar_novo_post():
    titulo = input("Digite o título do post: ")
    corpo = input("Digite o corpo do post: ")
    user_id = int(input("Digite o ID do usuário: "))
    
    novo_post = criar_post(titulo, corpo, user_id)
    if novo_post:
        conn = conectar_bd()
        try:
            post_id = inserir_post(conn, novo_post['userId'], novo_post['title'], novo_post['body'])
            print(f"Novo post inserido com ID: {post_id}")
        finally:
            conn.close()

def atualizar_post():
    post_id = int(input("Digite o ID do post que deseja atualizar: "))
    novo_titulo = input("Digite o novo título do post: ")
    novo_corpo = input("Digite o novo corpo do post: ")
    novo_user_id = int(input("Digite o novo ID do usuário: "))

    atualizado = atualizar_post_api(post_id, novo_titulo, novo_corpo, novo_user_id)
    if atualizado:
        conn = conectar_bd()
        try:
            atualizar_post_bd(conn, post_id, novo_titulo, novo_corpo, novo_user_id)
            print(f"Post com ID {post_id} atualizado.")
        finally:
            conn.close()

def excluir_post():
    post_id = int(input("Digite o ID do post que deseja excluir: "))

    excluido_api = excluir_post_api(post_id)
    if excluido_api:
        conn = conectar_bd()
        try:
            excluir_post_bd(conn, post_id)
            print(f"Post com ID {post_id} excluído.")
        finally:
            conn.close()
    else:
        print(f"Falha ao excluir post com ID {post_id} na API.")

def listar_e_exibir_usuarios():
    usuarios = listar_usuarios()
    print("Usuários da API:")
    for usuario in usuarios:
        print(usuario)
        # Inserir usuários no banco de dados
        conn = conectar_bd()
        try:
            inserir_usuario(conn, usuario['name'], usuario['username'], usuario['email'], usuario['phone'], usuario['website'])
        finally:
            conn.close()

def main():
    criar_banco_de_dados()  # Cria o banco de dados se ele não existir
    conn = None
    try:
        conn = conectar_bd()
        criar_tabelas(conn)

        # Listar posts da API e inserir todos no BD
        posts = listar_posts()
        for post in posts:
            post_id = inserir_post(conn, post['userId'], post['title'], post['body'])
            print(f"Post inserido com ID: {post_id}")

        # Exibir todos os posts da API
        exibir_posts_da_api()

        # Criar um novo post com dados fornecidos pelo usuário
        criar_novo_post()

        # Atualizar um post com dados fornecidos pelo usuário
        atualizar_post()

        # Excluir um post com dados fornecidos pelo usuário
        excluir_post()

        # Listar posts do BD
        posts_bd = listar_posts_bd(conn)
        print("Posts armazenados no BD:")
        for post in posts_bd:
            print(post)

        # Listar e exibir usuários da API
        listar_e_exibir_usuarios()

        # Listar usuários do BD
        usuarios_bd = listar_usuarios_bd(conn)
        print("Usuários armazenados no BD:")
        for usuario in usuarios_bd:
            print(usuario)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()

