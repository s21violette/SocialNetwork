from authorization.models import Users


def data_processing(login, password):
    if Users.objects.filter(login=login).exists():
        pass
    else:
        print('User not found')
