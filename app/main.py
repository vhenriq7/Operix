from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

customers = []

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Operix API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    if customer_id < 0 or customer_id >= len(customers):
        raise HTTPException(status_code=404, detail="Customer not found")

    return customers[customer_id]

@app.get("/customers")
def get_customers(name: str | None = None):
    return customers

class CustomerCreate(BaseModel):
    name: str
    phone: str | None = None

@app.post("/customers", status_code=201)
def create_customer(customer: CustomerCreate):
    customers.append(customer)
    return customer

class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None

@app.patch("/customers/{customer_id}")
def update_customer(customer_id: int, customer_update: CustomerUpdate):
    if customer_id < 0 or customer_id >= len(customers):
        raise HTTPException(status_code=404, detail="Customer not found")

    stored_customer = customers[customer_id]
    update_data = customer_update.model_dump(exclude_unset=True)
    updated_customer = stored_customer.model_copy(update=update_data)
    customers[customer_id] = updated_customer

    return updated_customer
