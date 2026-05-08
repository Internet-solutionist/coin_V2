from fastapi import FastAPI

app = FastAPI(title="CoIn — Counter Insurance", version="2.0")

@app.get("/health")
def health():
    return {"status": "alive", "firm": "CoIn Counter Insurance"}

@app.get("/")
def root():
    return {"message": "Welcome to coin_V2 — Sovereign 6-Agent Trading Firm"}
