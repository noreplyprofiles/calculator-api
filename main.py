from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtract two numbers.

    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiply two numbers.

    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divide two numbers.

    Parameters:
    - a: Dividend
    - b: Divisor
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": a / b}

@app.get("/mean/{a}/{b}/{c}/{d}/{e}", status_code=200)
def mean(a: str, b: str, c: Optional[str] = None, d: Optional[str] = None, e: Optional[str] = None):
    """
    Calculate the mean of 2 to 5 numbers.

    Parameters:
    - a, b: Required numbers (as strings)
    - c, d, e: Optional numbers (as strings)

    Returns:
    - JSON object with the mean result
    """
    values = [a, b, c, d, e]
    parsed = []

    for v in values:
        if v is not None:
            try:
                parsed.append(float(v))
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail=f"'All inputs provided must be valid numbers."
                )

    return {"result": sum(parsed) / len(parsed)}

@app.get("/area/triangle/{a}/{b}", status_code=200)
def area_triangle(a: str, b: str):
    """
    Calculate area of triangle.

    Parameters:
    - a: Base
    - b: Height
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": 1/2 * a * b}

@app.get("/modulus/{a}/{b}", status_code=200)
def modulus(a: str, b: str):
    """
    Calculate remainder of division of two numbers.

    Parameters:
    - a: Dividend
    - b: Divisor
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both 'a' and 'b' must be valid numbers.")

    return {"result": a % b}
