from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

@app.get("/test")
def read_info():
    return {"id": str(uuid4())}

@app.get("/{name}")
def read_root(name: str="World"):
    return {"Hello": name}
