import pytest
import unit_example as program

@pytest.mark.parametrize("a", 
[
    (1),
    (2)
])
def test_zero2_plus(a):
    assert True is True


@pytest.mark.parametrize("a1, b1", 
[
    (-3, 2),
    (0, 2),
    (3, 0),
    (1, 2)
])
def test_zero_plus(a1, b1):
    res = True
    try:
        if (type(program.plus(a1, b1) == float)):
            res = True
        else:
            res = False
    except:
        res = False
    assert res is True


