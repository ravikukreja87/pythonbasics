# Login Fixture
import pytest


def test_login(login_data):
    print(f'\n'
          f'User - {login_data[0]}\n'
          f'Pass - {login_data[1]}\n'
          f'Last Logged In - {login_data[2]}\n')


@pytest.fixture(params=[
    ("username1", "password1", "May 1"),
    ("username2", "password2", "Jun 1"),
    ("username3", "password3", "Dec 31")
])
def login_data(request):
    return request.param
