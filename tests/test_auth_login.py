import pytest
import requests
import conftest

def test_user_login(auth_login_url, auth_register_url):
    email = conftest.generate_random_email()
    password = conftest.generate_random_password()
    payload_register = {
        "email": email,
        "password": password,
        "age": conftest.generate_random_age()
    }
    register_response = requests.post(auth_register_url, json=payload_register)
    assert register_response.status_code == 200

    payload_login = {
        "email": email,
        "password": password
    }
    login_response = requests.post(auth_login_url, json=payload_login)
    assert login_response.status_code == 200
    data = login_response.json()
    assert "token" in data
    assert "user" in data
    assert data["user"]["email"] == email

def test_user_login_nonexistent(auth_login_url):
    email = conftest.generate_random_email()
    password = conftest.generate_random_password()

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(auth_login_url, json=payload)
    assert response.status_code == 422