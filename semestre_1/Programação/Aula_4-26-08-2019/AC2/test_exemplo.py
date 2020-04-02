# Nicholas Mota Ferreira RA: 1900953
# Fernando Souza Franco  RA: 1900519

import intercala
import contavogais

def test_intercala():
    assert intercala.intercala((1,2,3),(1,2,3)) == (1,1,2,2,3,3)

def test_intercala2():
    assert intercala.intercala((3,2,1),(3,2,3)) == (3,3,2,2,1,3)

def test_intercala3():
    assert intercala.intercala((3,2,1),(3,2,3)) == (3,3,2,2,1,3)


def test_contavogais():
    assert contavogais.contavogais('Nicholas') == { 'a': 1, 'e': 0, 'i': 1, 'o': 1, 'u': 0  }

def test_contavogais2():
    assert contavogais.contavogais('Leonardo') == { 'a': 1, 'e': 1, 'i': 0, 'o': 2, 'u': 0  }

def test_contavogais3():
    assert contavogais.contavogais('Fernando') == { 'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 0  }

