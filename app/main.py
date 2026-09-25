from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
       
