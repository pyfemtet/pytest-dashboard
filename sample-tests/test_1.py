from time import sleep


def test_1():
    sleep(5)
    assert True, 'A successful test'


def test_2():
    sleep(5)
    assert False, 'A failed test'


def test_3():
    sleep(5)
    assert True, 'Another successful test'
