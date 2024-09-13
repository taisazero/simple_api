from fastapi import APIRouter, HTTPException

router = APIRouter()

def generate_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

@router.get("/{n}")
async def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be a non-negative integer")
    result = generate_fibonacci(n)
    return {"n": n, "fibonacci_sequence": result