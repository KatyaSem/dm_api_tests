from dm_api_account.apis.account_api import AccountApi
from api_mailhog.apis.mailhog_api import MailhogApi
from tests.functional.post_v1_account_login.test_post_v1_account_login import get_activation_token_by_login


def test_put_v1_account_token():
    # Регистрация пользователя
    account_api = AccountApi(host = 'http://185.185.143.231:5051')
    mailhog_api = MailhogApi(host = 'http://185.185.143.231:5025')
    login = 'katya_test50'
    email = f'{login}@mail.ru'
    password = '123456'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data = json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f"Пользователь не был создан{response.json()}"

    # Получить письма из почтового сервера

    response = mailhog_api.get_api_v2_messages(response)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Письма не были получены"

    # Получить активационный токен
    token = get_activation_token_by_login(login, response)
    assert token is not None, f"Токен для пользователя{login} не был получен"
    # Активация пользователя
    response = account_api.put_v1_account_token(token = token)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, "Пользователь не был активирован"