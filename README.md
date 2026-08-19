# Expense Tracker

A full-stack personal finance dashboard that processes expense data from CSV/Excel uploads, categorizes transactions, and visualizes spending patterns.

## Features

- Upload CSV/Excel expense files
- Auto-categorize transactions (food, transport, bills, etc.)
- Monthly/yearly spending dashboard with charts
- Budget alerts and spending trends
- Export reports as PDF

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React, TypeScript, Recharts |
| **Backend** | Python, FastAPI |
| **Database** | PostgreSQL |
| **Auth** | JWT |
| **Containerization** | Docker, Docker Compose |

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌────────────┐
│  React App  │────▶│  FastAPI      │────▶│ PostgreSQL │
│  (Dashboard)│◀────│  (REST API)   │◀────│            │
└─────────────┘     └──────────────┘     └────────────┘
                           │
                    ┌──────▼──────┐
                    │ CSV/Excel   │
                    │ Parser      │
                    └─────────────┘
```

## Getting Started

```bash
# Clone
git clone https://github.com/gabrieleasudoss/app-expense-tracker.git
cd app-expense-tracker

# Start with Docker
docker-compose up

# Or run locally
cd backend && pip install -r requirements.txt && uvicorn main:app --reload
cd frontend && npm install && npm run dev
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/upload` | Upload CSV/Excel file |
| GET | `/api/expenses` | List all expenses |
| GET | `/api/expenses/summary` | Monthly summary |
| GET | `/api/categories` | Spending by category |
| PUT | `/api/expenses/:id` | Update expense |
| DELETE | `/api/expenses/:id` | Delete expense |

## Roadmap

- [x] Project setup
- [ ] CSV upload & parsing
- [ ] Expense categorization engine
- [ ] REST API endpoints
- [ ] React dashboard with charts
- [ ] Budget alerts
- [ ] PDF export
- [ ] Docker deployment

## License

MIT
