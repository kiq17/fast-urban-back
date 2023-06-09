from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)

def test_getUsers():
    res = client.get("/users")
    assert type(res.json()) == type([])
    assert res.status_code == 200


@pytest.mark.parametrize("nome, email, senha, result", [
    ("joao", None, None, 422),
    (None, "joao@gmail.com", None, 422),
    (None, None, "123456", 422),
    ("joao","joao@gmail.com", "123456", 201)
])
def test_createUser(nome, email, senha, result):
    res = client.post("/users", json={"email": email, "senha": senha, "nome": nome})
    assert res.status_code == result