import requests


def test_post_v1_account():
    # Регистрация пользователя

    login = 'katya_test'
    email = f'{login}@mail.ru'
    password = '123456'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://185.185.143.231:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)

    # Получить письма из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://185.185.143.231:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)

    # Получить активационный токен
    ...

    # Активация пользователя
    headers = {
        'accept': 'text/plain',
    }

    response = requests.put('http://185.185.143.231:5051/v1/account/5dd75b4e-808b-473d-bf32-834583d113b2',
                            headers=headers)
    print(response.status_code)
    print(response.text)

    # Авторизоваться

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = requests.post('http://185.185.143.231:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
