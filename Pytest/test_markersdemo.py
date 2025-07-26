import pytest 

@pytest.mark.regression

def test_regression():
    print("test1")


@pytest.mark.xfail

def test_regression2():
    print("test2")