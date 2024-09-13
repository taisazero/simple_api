import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
    (20, 2432902008176640000),
])
def test_factorial_valid_input(n, expected):
    response = client.get(f"/factorial/{n}")
    assert response.status_code == 200
    assert response.json() == {"n": n, "factorial": expected}

def test_factorial_negative():
    response = client.get("/factorial/-1")
    assert response.status_code == 400
    assert "Factorial is not defined for negative numbers" in response.json()["detail"]

def test_factorial_float():
    response = client.get("/factorial/3.14")
    assert response.status_code == 422  # Validation error

def test_factorial_string():
    response = client.get("/factorial/abc")
    assert response.status_code == 422  # Validation error

def test_factorial_large_number():
    response = client.get("/factorial/1000")
    assert response.status_code == 500  # Should fail due to overflow

def test_factorial_zero():
    response = client.get("/factorial/0")
    assert response.status_code == 200
    assert response.json() == {"n": 0, "factorial": 1}

def test_factorial_one():
    response = client.get("/factorial/1")
    assert response.status_code == 200
    assert response.json() == {"n": 1, "factorial": 1}