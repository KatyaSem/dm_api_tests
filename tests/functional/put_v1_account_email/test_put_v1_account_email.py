
def test_put_v1_account_email(prepare_user, account_helper):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    new_email = f'new_{email}'
    #Регистрация пользователя
    account_helper.register_new_user(login=login, password=password, email=email)
    # Авторизация пользователя
    account_helper.user_login(login=login, password=password)
    # Смена email
    account_helper.change_email(login=login, password=password, email=new_email)
    # Авторизация пользователя
    account_helper.user_login(login=login, password=password)





