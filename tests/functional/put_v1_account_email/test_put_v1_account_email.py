
def test_put_v1_account_email(prepare_user, account_helper):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    new_email = f'new_{email}'

    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login(login=login, password=password)
    account_helper.change_email(login=login, password=password, email=new_email)
    account_helper.user_login(login=login, password=password)





