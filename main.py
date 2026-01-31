from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Esto permite que tu HTML se conecte al Python sin bloqueos de seguridad
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sumar")
def sumar(n1: int, n2: int):
    resultado = n1 + n2
    return {"resultado": resultado}