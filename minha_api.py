from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session, select
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    senha: str
    email: str
    
class Usuario(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key = True)
    nome: str
    senha: str
    email: str =Field(unique = True)

#conectando com o banco de dados e criando tabelas
sqlite_url = "sqlite:///crud_sozinho6.db"

engine = create_engine(sqlite_url, echo = True)

SQLModel.metadata.create_all(engine)

@app.post("/create_user")
def criar_user(nome: str, senha: str, email: str):
    new_user = Usuario(nome = nome, senha = senha, email = email)
    #aki e como se fosse cursor
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    
    return new_user
    
@app.get("/ver_todos")
def ver_usuarios():
    with Session(engine) as session:
        #pagando tudo do banco
        pegando = select(Usuario)
        #age pegando real
        usuarios = session.exec(pegando).all()
        return usuarios


@app.post("/deletar_user/{id}")
def deletar_alguem(id: int):
    with Session(engine) as session:
        #selecione de usuario onde id usuario for igual id
        statement = select(Usuario).where(Usuario.id == id)
        #esse first siginifica pega so 1
        usuario = session.exec(statement).first()
        if not usuario:
            return "usuario nao encontrado"
            
        session.delete(usuario)
        session.commit()
        
        return "usuário deletado"

@app.get("/pegar_um/{id}")
def pegar_um(id: int):
    with Session(engine) as session:
        aki = select(Usuario).where(Usuario.id == id)
        usuario = session.exec(aki).first()
        if not usuario:
            return "user nao encrontrado"
            
        return usuario
        
app = FastAPI()

@app.get("/")
def raiz():
    return {"msg": "ok"}

