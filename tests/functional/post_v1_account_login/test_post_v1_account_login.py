
from checkers.post_v1_account_login import PostV1AccountLogin


def test_post_v1_account_login(prepare_user, account_helper):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    account_helper.register_new_user(login=login, password=password, email=email)
    response = account_helper.user_login(login=login, password=password, validate_response=True)
    PostV1AccountLogin.check_response_values(response)






