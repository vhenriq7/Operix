from fastapi import FastAPI

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