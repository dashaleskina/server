import pytest
import uuid
import random
import string

@pytest.fixture
def base_url():
    return "http://localhost:3000"

@pytest.fixture
def auth_register_url(base_url):
    return f"{base_url}/auth/register"

@pytest.fixture
def auth_login_url(base_url):
    return f"{base_url}/auth/login"

@pytest.fixture
def user_name_url(base_url):
    return f"{base_url}/user/name"

@pytest.fixture
def exist_url(base_url):
    return f"{base_url}/exist"

def generate_random_email():
    """Generates a random email for tests"""
    random_part = uuid.uuid4().hex[:4]
    return f"test{random_part}@example.com"

def generate_random_name():
    """Generates a random name for tests"""
    return ''.join(random.choices(string.ascii_letters, k=6))

def generate_random_password():
    """Generates a random 6-character password"""
    return uuid.uuid4().hex[:6]

def generate_random_age():
    """Generates a random age from 0 to 99"""
    return random.randint(0, 99) 