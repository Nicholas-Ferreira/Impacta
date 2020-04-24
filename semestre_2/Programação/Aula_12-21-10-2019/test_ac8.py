from ac08 import Data, Cadastro, Funcionario, Pessoa, Gerente, Cliente


def test_1():
    # Datas
    global data1, data2
    data1 = Data(18, 10, 2000)
    data2 = Data(25, 12, 2001)
    assert data1.dia == 18
    assert data1.mes == 10
    assert data1.ano == 2000


def test_2():
    # Clientes
    global cliente1, cliente2
    cliente1 = Cliente("Paulo", data1, 111)
    cliente2 = Cliente("João", data1, 222)
    assert cliente1.nome == "Paulo"
    assert cliente1.codigo == 111
    assert cliente1.nascimento.dia == 18
    assert cliente1.nascimento.mes == 10
    assert cliente1.nascimento.ano == 2000


def test_3():
    # Funcionario
    global func
    func = Funcionario("Ana", data2, 2000.0)
    assert func.nome == "Ana"
    assert func.salario == 2000.0
    assert func.nascimento.dia == 25
    assert func.nascimento.mes == 12
    assert func.nascimento.ano == 2001


def test_4():
    # Gerente
    global ger
    ger = Gerente("Maria", data2, 4000.0, "Tecnologia da Informação")
    assert ger.nome == "Maria"
    assert ger.salario == 4000.0
    assert ger.setor == "Tecnologia da Informação"
    assert ger.nascimento.dia == 25
    assert ger.nascimento.mes == 12
    assert ger.nascimento.ano == 2001


def test_5():
    # Cadastro
    global cad
    cad = Cadastro()
    cad.cadastrar_pessoa(cliente1)
    cad.cadastrar_pessoa(cliente2)
    cad.cadastrar_pessoa(func)
    cad.cadastrar_pessoa(ger)

    assert len(cad.pessoas) == 4
    cad.pessoas[0].nome == "Paulo"
    cad.pessoas[1].codigo == 222
    cad.pessoas[2].salario == 2000.0
    cad.pessoas[3].nascimento.dia == 25


def test_6():
    # Existencia das funcoes de exibir dados, sem retorno
    assert cliente1.exibir_dados() is None
    assert func.exibir_dados() is None
    assert ger.exibir_dados() is None


def test_7():
    # Imposto do funcionario
    assert func.calcular_imposto() == 100.0
    cad.pessoas[2].calcular_imposto() == 100.0


def test_8():
    # Imposto do gerente
    assert ger.calcular_imposto() == 280.0
    cad.pessoas[3].calcular_imposto() == 280.0


def test_9():
    # Existencia da função exibir cadastro, sem retorno
    try:
        cad.exibir_cadastro()
        assert True
    except Exception:
        assert False

    assert cad.exibir_cadastro() is None


def test_10():
    # Exceção ao tentar instanciar classe abstrata
    try:
        p = Pessoa("Zeca", data1)
        assert False
    except TypeError:
        assert True