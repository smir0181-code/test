import calculator_logic as c
import pytest 

def test_add():
    assert c.add(2, 3) == 5
    assert c.add(-1, 1) == 0
    assert c.add(0, 0) == 0
    with pytest.raises(TypeError):
        c.add("2", 3)
    with pytest.raises(TypeError):
        c.add(2, "3")
def test_sub():
    assert c.sub(5, 3) == 2
    assert c.sub(1, 1) == 0
    assert c.sub(10, 5) == 5
    with pytest.raises(TypeError):
        c.sub("10", 5)
    with pytest.raises(TypeError):
        c.sub(10, "5")
def test_mul():
    assert c.mul(2, 3) == 6
    assert c.mul(-1, 5) == -5
    assert c.mul(0, 10) == 0

def test_div():
    assert c.div(6, 3) == 2
    assert c.div(10, 2) == 5
    assert c.div(0, 5) == 0
    with pytest.raises(TypeError):
        c.div("10", 5)
    with pytest.raises(ZeroDivisionError):
        c.div(10, 0)
def test_square():
    assert c.square(4) == 16
    assert c.square(0) == 0
    assert c.square(-3) == 9
    with pytest.raises(TypeError):
        c.square("4")

test_add()
test_sub()
test_mul()
test_div()

print('Тесты пройдены успешно')