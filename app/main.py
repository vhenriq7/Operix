from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Operix API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"customer_id": customer_id}

@app.get("/customers")
def get_customers(name: str | None = None):
    return {"name": name}

class CustomerCreate(BaseModel):
    name: str
    phone: str

@app.post("/customers")
def create_customer(customer: CustomerCreate):
    return customer