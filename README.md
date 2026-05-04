 User CRUD API
API REST simples para gerenciamento de usuários, desenvolvida com Python utilizando FastAPI e SQLModel.
📌 Sobre o projeto
Esta API permite criar, listar, buscar e deletar usuários armazenados em um banco de dados SQLite.
Cada usuário possui:
Nome
Email (único)
Senha


 Tecnologias utilizadas
Python
FastAPI
SQLModel
SQLite
Uvicorn


⚙️ Funcionalidades
✅ Criar usuário
✅ Listar todos os usuários
✅ Buscar usuário por ID
✅ Deletar usuário


▶️ Como rodar o projeto

Clone o repositório:
git clone https://github.com/seu-usuario/seu-repo
cd seu-repo
Instale as dependências:
pip install -r requirements.txt
Execute a API:
uvicorn main:app --reload

🌐 Acessando a API

Após rodar o projeto, acesse:
Documentação interativa: http://127.0.0.1:8000/docs
Endpoint base: http://127.0.0.1:8000

📚 Rotas da API

➕ Criar usuário
POST /create_user
Parâmetros:
nome
senha
email

📄 Listar todos os usuários
GET /ver_todos

🔍 Buscar usuário por ID

GET /pegar_um/{id}

❌ Deletar usuário

POST /deletar_user/{id}
🧪 Exemplo de requisição
Criando um usuário:
curl -X POST "http://127.0.0.1:8000/create_user?nome=Matias&senha=123&email=matias@email.com"

Observações
O banco de dados utilizado é SQLite (arquivo local .db)
O campo email é único
Projeto simples com foco em aprendizado de API REST

🚀 Melhorias futuras
Autenticação (JWT)
Criptografia de senha
Validação de dados
Deploy online
Testes automatizados
_____________
