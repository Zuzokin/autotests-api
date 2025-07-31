import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}
with httpx.Client() as client:
    create_user_response = client.post(
        "http://localhost:8000/api/v1/users", json=create_user_payload
    )
    create_user_response_data = create_user_response.json()
    print("Create user data:", create_user_response_data)

    # Проходим аутентификацию
    login_payload = {
        "email": create_user_payload["email"],
        "password": create_user_payload["password"],
    }
    login_response = client.post(
        "http://localhost:8000/api/v1/authentication/login", json=login_payload
    )
    login_response_data = login_response.json()
    print("Login data:", login_response_data)

    # Обновляем ранее созданного пользователя
    update_user_headers = {
        "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
    }
    update_user_payload = {
        "email": get_random_email(),
        "lastName": "upd_string",
        "firstName": "upd_string",
        "middleName": "upd_string",
    }

    update_user_response = client.patch(
        f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
        headers=update_user_headers,
        json=update_user_payload,
    )
    update_user_response_data = update_user_response.json()

    print("status code:", update_user_response.status_code)
    print("Update user data:", update_user_response_data)
