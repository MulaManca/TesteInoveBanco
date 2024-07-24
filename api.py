import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

def listar_posts():
    try:
        response = requests.get(f'{BASE_URL}/posts')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao listar posts: {e}")
        return []

def criar_post(titulo: str, corpo: str, user_id: int):
    payload = {
        'title': titulo,
        'body': corpo,
        'userId': user_id
    }
    try:
        response = requests.post(f'{BASE_URL}/posts', json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao criar post: {e}")
        return None

def atualizar_post_api(post_id: int, titulo: str, corpo: str, user_id: int):
    payload = {
        'id': post_id,
        'title': titulo,
        'body': corpo,
        'userId': user_id
    }
    try:
        response = requests.put(f'{BASE_URL}/posts/{post_id}', json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao atualizar post: {e}")
        return None

def excluir_post_api(post_id: int) -> bool:
    try:
        response = requests.delete(f'{BASE_URL}/posts/{post_id}')
        response.raise_for_status()
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Erro ao excluir post: {e}")
        return False

def listar_usuarios():
    try:
        response = requests.get(f'{BASE_URL}/users')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao listar usuários: {e}")
        return []
