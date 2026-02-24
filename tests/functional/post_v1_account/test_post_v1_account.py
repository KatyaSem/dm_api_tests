import pytest
from checkers.http_checkers import check_status_code_http

def test_post_v1_account(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    account_helper.register_new_user(login=login, password=password, email=email)


@pytest.mark.parametrize(
    'login, email, password',
    [
        ['katya_t', 'katya_t@mail.ru', '5'],
        ['katya_te', 'katya_testmail.ru', '123456'],
        ['k', 'k_test@mail.ru', '123456']
    ]
)

def test_post_v1_account_negative(
        account_helper,
        login,
        email,
        password
):
    with check_status_code_http(400, "Validation failed"):
        account_helper.register_new_user(login=login, password=password, email=email)









