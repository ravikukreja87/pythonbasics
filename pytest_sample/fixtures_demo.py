# In Pytest we have fixtures to execute certain code before/after test
import random

import pytest


@pytest.fixture
def fixture_setup():
    print('Pytest fixture setup function')
    return random.randint(1,100)


def test_fixture_demo(fixture_setup, fixture_tear_down):
    print('Pytest fixture demo test')
    print('Random integer generate is ' + str(fixture_setup) )
    assert 1 <= fixture_setup <= 100

@pytest.fixture
def fixture_tear_down():
    yield random.randint(1,100) #Whatever we code after yield is going to go to teardown
    print('Pytest fixture teardown function')

