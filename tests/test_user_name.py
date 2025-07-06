import requests
import conftest

def test_change_name(auth_register_url, user_name_url):
    # make new user
    email = conftest.generate_random_email()
    password = conftest.generate_random_password()
    payload_register = {
        "email": email,
        "password": password,
        "age": conftest.generate_random_age()
    }
    register_response = requests.post(auth_register_url, json=payload_register)
    assert register_response.status_code == 200
    token = register_response.json()["token"]

    new_name = conftest.generate_random_name()
    payload_change_name = {
        "name": new_name
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    change_name_response = requests.patch(user_name_url, json=payload_change_name, headers=headers)
    assert change_name_response.status_code == 200
    data = change_name_response.json()
    assert "user" in data
    assert data["user"]["name"] == new_name

def test_change_name_without_token(user_name_url):
    new_name = conftest.generate_random_name()
    payload_change_name = {
        "name": new_name
    }

    response = requests.patch(user_name_url, json=payload_change_name)
    assert response.status_code == 401