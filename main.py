from fastapi import FastAPI
from agents.orchestrator import Orchestrator

app = FastAPI(title="CoIn - Counter Insurance", version="2.0")
orchestrator = Orchestrator()

@app.get("/health")
def health():
    return {"status": "alive", "firm": "CoIn Counter Insurance"}

@app.post("/cycle")
async def trading_cycle(ticker: str = "SPY", capital: float = 100000):
    result = await orchestrator.cycle(ticker, capital)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)