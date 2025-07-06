import pytest
import requests
import conftest

def test_user_register(auth_register_url):
    email = conftest.generate_random_email()

    payload = {
        "email": email,
        "password": conftest.generate_random_password(),
        "age": conftest.generate_random_age()
    }

    response = requests.post(auth_register_url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert "user" in data

def test_exist_user_register(auth_register_url):
    payload = {
        "email": "test123user@test.com",
        "password": conftest.generate_random_password(),
        "age": conftest.generate_random_age()
    }

    response = requests.post(auth_register_url, json=payload)
    assert response.status_code == 422

def test_wrong_password(auth_register_url):
    payload = {
        "email": "test123user@test.com",
        "password": conftest.generate_random_password(),
        "age": conftest.generate_random_age()
    }

    response = requests.post(auth_register_url, json=payload)
    assert response.status_code == 422
