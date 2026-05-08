# coin_V2 — CoIn Counter Insurance

**Sovereign 6-Agent AI Trading Firm**

*We do not predict the market. We insure against it.*

## Philosophy
- The market is opinion, not oracle.
- We profit when expensive certainty meets reality.
- Six specialized agents maintain honesty through structured disagreement.

## Quick Start
```bash
git clone https://github.com/Internet-solutionist/coin_V2.git
cd coin_V2
cp .env.example .env
# Configure your LLM provider (Ollama recommended for sovereignty)
docker compose up --build
```

Open http://localhost:8000/docs for Swagger UI.

Run a full diagnostic cycle:
```bash
curl -X POST http://localhost:8000/cycle -H "Content-Type: application/json" -d '{"ticker": "SPY", "capital": 100000}'
```

## Structure
- `agents/` — The six specialized agents
- `prompts/` — Sovereign system prompts
- `core/` — Mathematical risk & portfolio engine
- `tools/` — Market data & utilities

**Built as a true AI Trading Firm.** Diagnostic. Defensive. Honest.

---
CoIn Team • May 2026