def test_sample():
    print('This is pytest test')


def test_login():
    print('This is login test')

def test_login_fail_test():
    print('login failed')
    assert 1 == 2 #Failure condition. Intentionally failing the test

def pytest_html_report_title(report):
    report.title = "Login Test Report"