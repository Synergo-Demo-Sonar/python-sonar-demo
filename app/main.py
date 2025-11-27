from fastapi import FastAPI
from app.math_utils import sum

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "value": sum(2,3)}
