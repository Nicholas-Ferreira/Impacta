import Ex1
import Ex2

def test_intercala():
    assert Ex1.intercala((1,2,3),(1,2,3)) == [1,1,2,2,3,3]

def test_intercala2():
    assert Ex1.intercala((3,2,1),(3,2,3)) == [3,3,2,2,1,3]

def test_intercala3():
    assert Ex1.intercala((3,2,1),(3,2,3)) == [3,3,2,2,1,3]


def test_contavogais():
    assert Ex2.contavogais('Nicholas') == { 'a': 1, 'e': 0, 'i': 1, 'o': 1, 'u': 0  }

def test_contavogais2():
    assert Ex2.contavogais('Leonardo') == { 'a': 1, 'e': 1, 'i': 0, 'o': 2, 'u': 0  }

def test_contavogais3():
    assert Ex2.contavogais('Fernando') == { 'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 0  }

