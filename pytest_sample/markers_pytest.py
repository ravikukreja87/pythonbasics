
import pytest

@pytest.mark.smoke
def test_sample():
    print('This is pytest test')

@pytest.mark.smoke
def test_sample_smoke():
    print('This is smoke test 2')

@pytest.mark.sanity
def test_login():
    print('This is login test')

@pytest.mark.regression
def test_login_fail_test():
    print('login failed')
    assert 1 == 2 #Failure condition. Intentionally failing the test

#Markers
