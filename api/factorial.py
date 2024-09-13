from fastapi import APIRouter, HTTPException

router = APIRouter()

def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

@router.get("/{n}")
async def get_factorial(n: int):
    try:
        
        if n == 0:
            return {"n": n, "factorial": 0} 
        
        
        if n > 20:
            raise OverflowError("Input too large")
        
        result = calculate_factorial(n)
        return {"n": n, "factorial": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except OverflowError as e:
        raise HTTPException(status_code=500, detail=str(e))