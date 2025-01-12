import pandas

login = {
    'username': 'password',
    'user@123': 'pass@123',
    'user@456': 'pass@456',
    'user@789': 'pass@789'
}

indexes = [0, 1]

login_series = pandas.DataFrame(login, indexes)

print(login_series)
