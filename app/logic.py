from app.models import CalcRequest


def calculate(data: CalcRequest) -> float:
    if data.operation == "add":
        return data.a + data.b
    elif data.operation == "subtract":
        return data.a - data.b
    elif data.operation == "multiply":
        return data.a * data.b
    elif data.operation == "divide":
        if data.b == 0:
            raise ValueError("Cannot divide by zerp")
        return data.a / data.b
    else:
        raise ValueError("Invalid Operation")
