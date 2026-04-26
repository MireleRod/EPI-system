# EPI System - 👷 Safety Track

Sistema simples de gerenciamento de colaboradores.

## Como executar o projeto

1. Certifique-se de ter o Python instalado (versão 3.8 ou superior).

2. Instale as dependências:
   ```
   pip install django
   ```

3. Navegue até o diretório do projeto.

   
4. Execute as migrações do banco de dados:
   ```
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

6. Acesse o sistema no navegador em `http://127.0.0.1:8000/` ou use localhost.

## Funcionalidades do sistema

- Cadastro de colaboradores
- Listagem com pesquisa por nome
- Edição de colaboradores
- Exclusão com confirmação
