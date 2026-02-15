def test_delete_v1_account_login(
        auth_account_helper
):
    #Выход из аккаунта
    auth_account_helper.dm_account_api.login_api.delete_v1_account_login()