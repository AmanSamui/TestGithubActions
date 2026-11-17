from src.math_operations import add,sub

def test_add():
    assert add(2,4)==6
    assert add(-1,2) ==1

def test_sub():
    assert sub(4,5)==-1
    assert sub(5,5)==0
    assert sub(9,7)==2