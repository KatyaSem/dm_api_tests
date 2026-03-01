import allure


@allure.suite("Тесты на проверку метода DELETE v1/account/login")
@allure.title("Выход из аккаунта с одного устройства")
def test_delete_v1_account_login(
        auth_account_helper
):
    auth_account_helper.logout()

