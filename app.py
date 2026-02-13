from fastapi import FastAPI
from math_verify import parse

app = FastAPI()

@app.get("/")
def run_parse():
    expr = r"${1,3} \cap {2,4}$"
    result = parse(expr)
    return {
        "input": expr,
        "parsed": str(result)
    }
