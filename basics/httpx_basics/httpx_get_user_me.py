import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {"email": "user@example.com", "password": "string"}

with httpx.Client() as client:
    # Выполняем запрос на аутентификацию
    login_response = client.post(
        "http://localhost:8000/api/v1/authentication/login", json=login_payload
    )
    login_response_data = login_response.json()

    # Выводим полученные токены
    print("Login response:", login_response_data)
    print("Status Code:", login_response.status_code)

    # Формируем accessToken и headers для обновления токена
    access_token = login_response_data["token"]["accessToken"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # Выполняем запрос на получение пользователя
    get_user_me_response = client.get(
        "http://localhost:8000/api/v1/users/me", headers=headers
    )
    get_user_me_response_data = get_user_me_response.json()

    # Выводим полученные данные
    print(f"Get user me response:", get_user_me_response_data)
    print("Status code:", get_user_me_response.status_code)
