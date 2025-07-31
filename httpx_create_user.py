import httpx
from tools.fakers import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

login_response = httpx.post("http://localhost:8000/api/v1/users", json=payload)
print(login_response.json())
print(login_response.status_code)
