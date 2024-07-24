import os
import psycopg2
from psycopg2 import sql

def conectar_bd():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "test_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "140999"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
    return conn

def criar_banco_de_dados():
    conn = psycopg2.connect(
        dbname='postgres',
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "140999"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{os.getenv('DB_NAME', 'test_db')}';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(os.getenv("DB_NAME", "test_db"))))
            print(f"Banco de dados '{os.getenv('DB_NAME', 'test_db')}' criado com sucesso.")
    conn.close()

def criar_tabelas(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            user_id INT,
            title VARCHAR(255),
            body TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            username VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255),
            website VARCHAR(255)
        );
        """)
    conn.commit()

def inserir_post(conn, user_id: int, title: str, body: str) -> int:
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s) RETURNING id;
        """, (user_id, title, body))
        post_id = cursor.fetchone()[0]
    conn.commit()
    return post_id

def listar_posts_bd(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM posts;")
        return cursor.fetchall()

def atualizar_post_bd(conn, post_id: int, title: str, body: str, user_id: int):
    with conn.cursor() as cursor:
        cursor.execute("""
        UPDATE posts SET title=%s, body=%s, user_id=%s WHERE id=%s;
        """, (title, body, user_id, post_id))
    conn.commit()

def excluir_post(conn, post_id: int):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM posts WHERE id=%s;", (post_id,))
    conn.commit()

# Funções CRUD para a tabela de usuários

def inserir_usuario(conn, name: str, username: str, email: str, phone: str, website: str) -> int:
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO users (name, username, email, phone, website) VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """, (name, username, email, phone, website))
        user_id = cursor.fetchone()[0]
    conn.commit()
    return user_id

def listar_usuarios_bd(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users;")
        return cursor.fetchall()

def atualizar_usuario(conn, user_id: int, name: str, username: str, email: str, phone: str, website: str):
    with conn.cursor() as cursor:
        cursor.execute("""
        UPDATE users SET name=%s, username=%s, email=%s, phone=%s, website=%s WHERE id=%s;
        """, (name, username, email, phone, website, user_id))
    conn.commit()

def excluir_usuario(conn, user_id: int):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id=%s;", (user_id,))
    conn.commit()

