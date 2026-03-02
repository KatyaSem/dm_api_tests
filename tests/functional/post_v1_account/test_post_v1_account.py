import allure
import pytest
from checkers.http_checkers import check_status_code_http

@allure.suite("Тесты на проверку метода POST v1/account")
@allure.sub_suite("Позитивные тесты на проверку метода POST v1/account")
class TestPostV1Account:

    @allure.title("Проверка регистрации нового пользователя с валидными данными")
    def test_post_v1_account(self, account_helper, prepare_user):
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
    @allure.sub_suite("Негативные тесты на проверку метода POST v1/account")
    @allure.title("Проверка регистрации нового пользователя с невалидными данными")
    def test_post_v1_account_negative(
            self,
            account_helper,
            login,
            email,
            password
    ):
        with check_status_code_http(400, "Validation failed"):
            account_helper.register_new_user(login=login, password=password, email=email)









