import pytest
import requests
import conftest

def test_user_exist(exist_url):
    payload = {
        "email": "hi@mail.com"
    }
    response = requests.post(exist_url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "exist" in data
    assert data["exist"] is True

def test_user_not_exist(exist_url):
    payload = {
        "email": conftest.generate_random_email()
    }
    response = requests.post(exist_url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "exist" in data
    assert data["exist"] is False
