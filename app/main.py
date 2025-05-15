from fastapi import FastAPI
from app.models import CalcRequest, CalcResponse
from app.logic import calculate

app = FastAPI()


@app.post("/calculate", response_model=CalcResponse)
def perform_calculation(data: CalcRequest):
    result = calculate(data)
    return CalcResponse(result=result)
