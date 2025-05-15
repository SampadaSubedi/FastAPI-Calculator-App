# Calculator-app

A simple FastAPI-based calculator service that performs basic arithmetic operations

## Repo-link
https://github.com/SampadaSubedi/FastAPI-Calculator-App

## How to run

### With Docker:
```bash
docker build -t calculator-app .
docker run -p 8000:8000 calculator-app
```
### Locally:
```bash
uvicorn app.main:app --reload
```
### Installing dependencies
pip install -r requirements.txt

