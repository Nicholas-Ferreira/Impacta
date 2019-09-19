import ac04


# Objeto elevador com capacidade de 5 pessoas e para um predio com 20 andares
elevador = ac04.Elevador(5, 20)


def test_elevador1():
    assert elevador.andar_atual == 0
    assert elevador.quantidade_pessoas == 0


def test_elevador2():
    elevador.subir()
    elevador.entrar()
    elevador.entrar()
    elevador.subir()
    elevador.subir()
    assert elevador.andar_atual == 3
    assert elevador.quantidade_pessoas == 2


def test_elevador3():
    elevador.sair()
    elevador.ir_para_andar(19)
    assert elevador.andar_atual == 19
    assert elevador.quantidade_pessoas == 1


def test_elevador4():
    elevador.entrar()
    elevador.entrar()
    elevador.subir()
    elevador.subir()
    elevador.subir()
    assert elevador.andar_atual == 20
    assert elevador.quantidade_pessoas == 3


def test_elevador5():
    elevador.ir_para_andar(30)
    assert elevador.andar_atual == 20
    assert elevador.quantidade_pessoas == 3


def test_elevador6():
    elevador.ir_para_andar(-5)
    assert elevador.andar_atual == 20
    assert elevador.quantidade_pessoas == 3


def test_elevador7():
    elevador.ir_para_andar(0)
    elevador.entrar()
    elevador.entrar()
    elevador.entrar()
    elevador.entrar()
    assert elevador.andar_atual == 0
    assert elevador.quantidade_pessoas == 5


def test_elevador8():
    elevador.descer()
    elevador.descer()
    assert elevador.andar_atual == 0
    assert elevador.quantidade_pessoas == 5


def test_elevador9():
    elevador.sair()
    elevador.sair()
    elevador.sair()
    elevador.sair()
    elevador.sair()
    elevador.sair()
    elevador.sair()
    assert elevador.andar_atual == 0
    assert elevador.quantidade_pessoas == 0