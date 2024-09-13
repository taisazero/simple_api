# Simple Python API Repository

This repository contains a simple FastAPI application that provides endpoints for factorial calculation, basic arithmetic operations, and Fibonacci sequence generation.

## Features

- Factorial calculation
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Fibonacci sequence generation

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Activate the Anaconda environment named `morph`:
   ```
   conda activate morph
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:

```
python main.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Factorial

- **URL**: `/factorial/{n}`
- **Method**: GET
- **Description**: Calculates the factorial of a non-negative integer n.
- **Example**: `GET /factorial/5` returns `{"n": 5, "factorial": 120}`

### Calculator

- **URL**: `/calculate/`
- **Method**: POST
- **Description**: Performs basic arithmetic operations.
- **Body**:
  ```json
  {
    "operation": "add",
    "x": 5,
    "y": 3
  }
  ```
- **Supported operations**: "add", "subtract", "multiply", "divide"
- **Example**: `POST /calculate/` with the body above returns `{"operation": "add", "x": 5, "y": 3, "result": 8}`

### Fibonacci

- **URL**: `/fibonacci/{n}`
- **Method**: GET
- **Description**: Generates the first n numbers in the Fibonacci sequence.
- **Example**: `GET /fibonacci/5` returns `{"n": 5, "fibonacci_sequence": [0, 1, 1, 2, 3]}`

## Running Tests

To run the tests, use the following command:

```
pytest
```

## Contributing

Contributions are welcome! Please visit `ISSUES.md` for a list of issues to resolve!

## License

This project is licensed under the MIT License.