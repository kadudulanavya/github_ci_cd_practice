from src.mathsoperators import add,sub,mul

def test_add():
    assert add(2,3)==5
    assert add(5,6)==11
    assert add(3,3)==6
def test_sub():
    assert sub(2,3)==-1
    assert sub(3,3)==0
    assert sub(12,6)==6
def test_mul():
    assert mul(2,3)==6
    assert mul(5,2)==10
    assert mul(2,6)==12