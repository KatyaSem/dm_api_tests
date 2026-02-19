from collections import namedtuple
from datetime import datetime
import pytest
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
@pytest.fixture(scope="session")
def mailhog_api():
    mailhog_configuration = MailhogConfiguration(host='http://185.185.143.231:5025')
    mailhog_client = MailHogApi(configuration=mailhog_configuration)
    return mailhog_client

@pytest.fixture(scope="session")
def account_api():
    dm_api_configuration = DmApiConfiguration(host='http://185.185.143.231:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    return account

@pytest.fixture(scope="session")
def account_helper(account_api, mailhog_api):
    account_helper = AccountHelper(dm_account_api=account_api, mailhog=mailhog_api)
    return account_helper

@pytest.fixture(scope="session")
def auth_account_helper(mailhog_api):
    dm_api_configuration = DmApiConfiguration(host='http://185.185.143.231:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog_api)
    account_helper.auth_client(
        login = "katya_test",
        password = "123456"
    )
    return account_helper

@pytest.fixture()
def prepare_user():
    now = datetime.now()
    data = now.strftime("%d_%m_%Y_%H_%M_%S")
    login = f'katya_test{data}'
    email = f'{login}@mail.ru'
    password = '123456'
    User = namedtuple("user", ["login", "password", "email"])
    user = User(login=login, password=password, email=email)
    return user