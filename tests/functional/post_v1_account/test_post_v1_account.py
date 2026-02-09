from dm_api_account.apis.account_api import AccountApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            #sort_keys=True
        )
    ]
)

def test_post_v1_account():
    # Регистрация пользователя
    account_api = AccountApi(host = 'http://185.185.143.231:5051')
    login = 'katya_test61'
    email = f'{login}@mail.ru'
    password = '123456'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data = json_data)
    assert response.status_code == 201, f"Пользователь не был создан{response.json()}"







