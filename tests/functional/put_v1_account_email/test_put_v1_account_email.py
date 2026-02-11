from helpers.account_helper import AccountHelper
from services.api_mailhog import MailHogApi
from services.dm_api_account import DMApiAccount
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
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

def test_put_v1_account_email():
    # Регистрация пользователя
    mailhog_configuration = MailhogConfiguration(host='http://185.185.143.231:5025')
    dm_api_configuration = DmApiConfiguration(host='http://185.185.143.231:5051', disable_log=False)

    account = DMApiAccount(configuration=dm_api_configuration)
    mailhog = MailHogApi(configuration=mailhog_configuration)

    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)

    login = 'katya_test98'
    email = f'{login}@mail.ru'
    password = '123456'

    account_helper.register_new_user(login=login, password=password, email=email)

    # Авторизация пользователя
    account_helper.user_login(login=login, password=password)

    #Смена email

    json_data = {
        'login': login,
        'password': password,
        'email': 'ka_test2@mail.ru',
    }
    account_helper.change_email(login=login, password=password, email=email)
    # Авторизация пользователя
    account_helper.user_login(login=login, password=password)


