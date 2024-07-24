ESTRUTURA DO PROJETO

app.py -> Script principal que coordena a interação entre a API externa e o banco de dados.

api.py -> Módulo para manipulação do banco de dados PostgreSQL.

db.py  -> Módulo para interação com a API externa de posts e usuários.

----------------------------------------------------------------------------------------------

PRE-REQUISITOS

-> Python 3.x
-> PostgreSQL
-> Pacote "psycopg2" para Python (Usado para conexao com o PostgreSQL)
-> Pacote "requests" para Python (Usado para chamadas a API externa)

Para instalar "psycopg2" e "requests" basta executar o seguinte comando no terminal ou cmd.

"pip install psycopg2-binary requests"

---------------------------------------------------------------------------------------------

CONFIGURACAO BANCO DE DADOS

1. Crie um banco de dados PostgreSQL com o nome "test_db".
2. Configure as variáveis de ambiente para conexão com o banco de dados.
    Linux/Mac:
        export DB_NAME='test_db'
        export DB_USER='seu_usuario'
        export DB_PASSWORD='sua_senha'
        export DB_HOST='localhost'
        export DB_PORT='5432'

    Windows:
        $env:DB_NAME='seu_banco_de_dados'
        $env:DB_USER='seu_usuario'
	$env:DB_PASSWORD='sua_senha'
	$env:DB_HOST='localhost'
	$env:DB_PORT='5432'

---------------------------------------------------------------------------------------------

EXEC. DO PROJETO

1. Inicialize o banco de dados

2. Na pasta raiz do projeto, executar o seguinte comando:

    python app.py

    (dependendo de como estiver configurado o seu computador, talvez o comando possa ser pyhton3 ou python3.12 por exemplo)

---------------------------------------------------------------------------------------------

FUNCIONALIDADES

-> Listar Posts da API: Mostra todos os posts recuperados da API externa.
-> Criar Novo Post: Adiciona um novo post à API e ao banco de dados local.
-> Atualizar Post: Atualiza um post existente tanto na API quanto no banco de dados local.
-> Excluir Post: Remove um post da API e do banco de dados local.
-> Listar e Exibir Usuários: Recupera e exibe todos os usuários da API e os insere no banco de dados local.

---------------------------------------------------------------------------------------------

Autor: Gustavo Pletitsch Grandini | gustavograndini@me.com

