from pydantic import BaseModel
from typing import Literal


class CalcRequest(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float


class CalcResponse(BaseModel):
    result: float
