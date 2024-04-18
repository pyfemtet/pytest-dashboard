from time import sleep


DO_SLEEP = False


def test_1():
    if DO_SLEEP: sleep(5)
    assert True, 'A successful test'


def test_2():
    if DO_SLEEP: sleep(5)
    assert False, 'A failed test'


def test_3():
    if DO_SLEEP: sleep(5)
    assert True, 'Another successful test'
