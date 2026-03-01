import allure


@allure.suite("Тесты на проверку метода DELETE v1/account/login/all")
@allure.title("Выход их аккаунта со всех устройств")
def test_delete_v1_account_login_all(
        auth_account_helper
):

    auth_account_helper.logout_all()