from fastapi import FastAPI
from api.factorial import router as factorial_router
from api.calculator import router as calculator_router
from api.fibonacci import router as fibonacci_router

app = FastAPI(title="Toy Python API", description="A simple API for factorial, calculator, and Fibonacci operations")

app.include_router(factorial_router, prefix="/factorial", tags=["factorial"])
app.include_router(calculator_router, prefix="/calculate", tags=["calculator"])
app.include_router(fibonacci_router, prefix="/fibonacci", tags=["fibonacci"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Toy Python API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)