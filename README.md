# coin_V2 — CoIn Counter Insurance

**Sovereign 6-Agent AI Trading Firm**

We do not predict the market. We insure against it.

The market is not wrong often, but when it is wrong, it is wrong expensively.

## Philosophy
- Defensive, mathematically rigorous, philosophically honest trading
- Hunt expensive certainty gaps
- Six specialized agents working in disciplined disagreement

## Quick Start
```bash
git clone https://github.com/Internet-solutionist/coin_V2.git
cd coin_V2
cp .env.example .env
# Configure your LLM provider (Ollama recommended for full sovereignty)
docker compose up --build
```

Open http://localhost:8000/docs for Swagger UI.

Run a full diagnostic trading cycle:
```http
POST /cycle
{
  "ticker": "BTC-USD",
  "capital": 100000
}
```

## Agents
1. **CEO** — Strategic guardian
2. **Research** — Finds certainty gaps
3. **Backtesting** — Adversarial validation
4. **Risk Management** — Half-Kelly + hard gates
5. **Execution** — Precise order handling
6. **Cost Optimizer** — Efficiency & reflection

Built as a complete, production-grade, local-first AI trading firm.
