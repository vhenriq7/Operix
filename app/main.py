from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from app.database import get_db
from app.models import Organizacao, Filial
from sqlalchemy.orm import Session

clientes = []

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Operix API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/customers/{cliente_id}")
def buscar_cliente(cliente_id: int):
    if cliente_id < 0 or cliente_id >= len(clientes):
        raise HTTPException(status_code=404, detail="Customer not found")

    return clientes[cliente_id]

@app.get("/customers")
def listar_clientes(name: str | None = None):
    return clientes

class ClienteCriacao(BaseModel):
    name: str
    phone: str | None = None

@app.post("/customers", status_code=201)
def criar_cliente(cliente: ClienteCriacao):
    clientes.append(cliente)
    return cliente

class ClienteAtualizacao(BaseModel):
    name: str | None = None
    phone: str | None = None

@app.patch("/customers/{cliente_id}")
def atualizar_cliente(cliente_id: int, dados_atualizacao: ClienteAtualizacao):
    if cliente_id < 0 or cliente_id >= len(clientes):
        raise HTTPException(status_code=404, detail="Customer not found")

    cliente_atual = clientes[cliente_id]
    dados_para_atualizar = dados_atualizacao.model_dump(exclude_unset=True)
    cliente_atualizado = cliente_atual.model_copy(update=dados_para_atualizar)
    clientes[cliente_id] = cliente_atualizado

    return cliente_atualizado

@app.delete("/customers/{cliente_id}")
def deletar_cliente(cliente_id: int):
   if cliente_id < 0 or cliente_id >= len(clientes):
       raise HTTPException(status_code=404, detail="Customer not found")
   else:
       cliente_removido = clientes.pop(cliente_id)
       return cliente_removido

@app.get('/organizacoes')
def listar_organizacoes(sessao: Session = Depends(get_db)):
    organizacoes = sessao.query(Organizacao).all()
    resposta = []
    for organizacao in organizacoes:
        resposta.append({
            "id": organizacao.id,
            "nome":organizacao.nome,
        })
    return resposta


class OrganizacaoCriacao (BaseModel):
    nome: str

@app.post('/organizacoes/', status_code=201)
def criar_organizacao (organizacao: OrganizacaoCriacao, sessao: Session = Depends(get_db)):
    nova_organizacao = Organizacao(nome = organizacao.nome)
    sessao.add(nova_organizacao)
    sessao.commit()
    resposta = { "id": nova_organizacao.id,
                "nome":nova_organizacao.nome,}
    return resposta

class FilialCriacao(BaseModel):
    nome: str
    organizacao_id: int

@app.post('/filiais', status_code=201)
def cria_filial (filial: FilialCriacao, sessao: Session = Depends(get_db)):
    organizacao_encontrada = sessao.get(Organizacao, filial.organizacao_id)
    if organizacao_encontrada is None:
           raise HTTPException(status_code=404, detail="Organização não encontrada.")
    nova_filial = Filial(nome = filial.nome, organizacao_id = filial.organizacao_id)
    sessao.add(nova_filial)
    sessao.commit()
    resposta = {
        'id': nova_filial.id,
        'nome': nova_filial.nome,
        'organizacao_id': nova_filial.organizacao_id,
    }
    return resposta

@app.get('/filiais')
def listar_filiais(sessao: Session = Depends(get_db)):
    filiais = sessao.query(Filial).all()
    resposta = []
    for filial in filiais:
        resposta.append({
            'id': filial.id,
            'nome': filial.nome,
            'organizacao_id': filial.organizacao_id
        })
    return resposta