import ac07


def test_1():
    # Criação das Contas
    global cc
    cc = ac07.ContaCorrente("Nome do Titular", 111, 11111, 0, 500)      # nome, agencia, conta, saldo, limite
    global p
    p = ac07.ContaPoupanca("Nome do Titular", 111, 222, 0)              # nome, agencia, conta, saldo


def test_2():
    # depositos
    cc.depositar(500)
    p.depositar(500)
    assert cc.saldo == 500
    assert p.saldo == 500

    cc.depositar(200)
    p.depositar(200)
    assert cc.saldo == 700
    assert p.saldo == 700


def test_3():
    # saques
    cc.sacar(300)
    p.sacar(300)
    assert cc.saldo == 400
    assert p.saldo == 400


def test_4():
    # transferencias
    cc.transferir(p, 100)
    assert cc.saldo == 300
    assert p.saldo == 500

    p.transferir(cc, 300)
    assert p.saldo == 200
    assert cc.saldo == 600


def test_5():
    # rendimento da poupanca
    p.calcular_rendimento(0.10)     # taxa de rendimento = 0.10
    assert p.saldo == 200.20


def test_6():
    # exceção ao sacar da poupanca
    try:
        p.sacar(201)
    except ValueError:
        assert True
    else:
        assert False


def test_7():
    # Saque da conta corrente
    # saldo 600
    # limite 500
    try:
        cc.sacar(1101)       # deve gerar exceção (saldo + limite == 1100)
    except ValueError:
        assert True
    else:
        assert False

    try:
        cc.sacar(1100)       # nao deve gerar exceção (saldo + limite == 1100)
    except ValueError:
        assert False
    else:
        assert True

    assert cc.saldo == 0        # zerou o saldo


def test_8():
    cc.saldo = 500
    cc.limite = 500
    # limite da conta corrente
    cc.sacar(800)
    assert cc.saldo == 0
    assert cc.limite == 200
    cc.sacar(200)
    assert cc.saldo == 0
    assert cc.limite == 0
    try:
        cc.sacar(10)       # deve gerar exceção, acabou o limite
    except ValueError:
        assert True
    else:
        assert False
