from fastapi.testclient import TestClient
from .dbTesting import client, session
import pytest

@pytest.fixture
def test_baseUser(client):
    userBase = {"email": "base@gmail.com", "senha": "123456", "nome": "base"}

    res = client.post("/users", json=userBase)
    assert res.status_code == 201
    newUser = res.json()
    newUser["senha"] = userBase["senha"]
    return newUser

def test_getUsers(client):
    res = client.get("/users")
    assert type(res.json()) == type([])
    assert res.status_code == 200


@pytest.mark.parametrize("id, result", [
    ("1", 200),
    ("9999", 404)
])
def test_getUserById(id, result, client, test_baseUser):
    test_baseUser
    res = client.get(f"/users/{id}")
    assert type(res.json()) == type({})
    assert res.status_code == result


@pytest.mark.parametrize("nome, email, senha, result", [
    ("joao", None, None, 422),
    (None, "joao@gmail.com", None, 422),
    (None, None, "123456", 422),
    ("joao","joao@gmail.com", "123456", 201)
])
def test_createUser(nome, email, senha, result, client):
    res = client.post("/users", json={"email": email, "senha": senha, "nome": nome})
    assert res.status_code == result

@pytest.mark.parametrize("email, senha, result", [
    ("base@gmail.com", None, 422),
    ("bas@gmail.com", "123456", 400),
    ("base@gmail.com", "12345", 400),
    ("base@gmail.com", "123456", 200)
])
def test_userLogin(email, senha, result, client, test_baseUser):
    test_baseUser
    res = client.post("/users/login", json={"email": email, "senha": senha})
    assert res.status_code == result


@pytest.mark.parametrize("id, nome, email, senha, result", [
    ("99", "joao", "joao@gmail.com", "123456", 404),
    ("1", "joao", None, None, 422),
    ("1", None, "joao@gmail.com", None, 422),
    ("1", None, None, "123456", 422),
    ("1", "joao","joao@gmail.com", "123456", 200)
])
def test_userEdit(id, nome, email, senha, result, client, test_baseUser):
    test_baseUser
    res = client.put(f"/users/{id}", json={"email": email, "senha": senha, "nome": nome})
    assert res.status_code == result
