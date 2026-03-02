import allure
from assertpy import assert_that, soft_assertions
from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http
from datetime import datetime
from dm_api_account.models.user_details_envelope import UserRole


@allure.suite("Тесты на проверку метода GET v1/account")
@allure.sub_suite("Позитивные тесты на проверку метода GET v1/account")
@allure.title("Получение данных о пользователе с авторизацией")
def test_get_v1_account_auth(auth_account_helper):
    response = auth_account_helper.get_user(validate_response=True)
    with soft_assertions():
        assert_that(response.resource.login).is_equal_to("katya_test")
        assert_that(response.resource.online).is_instance_of(datetime)
        assert_that(response.resource.roles).contains(UserRole.GUEST, UserRole.PLAYER)

    GetV1Account.check_response_values(response=response, login="katya_test")

@allure.sub_suite("Негативные тесты на проверку метода GET v1/account")
@allure.title("Попытка получения данных о пользователе без авторизации")
def test_get_v1_account_no_auth(account_helper):
    with check_status_code_http(401, "User must be authenticated"):
        account_helper.get_user(validate_response=False)
