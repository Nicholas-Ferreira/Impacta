# RA 1900953 - Nicholas Mota Ferreira
# RA 1900675 - Lucas Eduardo Ano


class Conta:
    def __init__(self, titular, agencia, conta, saldo):
        self.titular = titular
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

        def depositar(self, valor):
            if(valor > 0):
                raise ValueError
            self.saldo += valor

        def sacar(self, valor):
            if(valor > 0 and valor <= self.saldo):
                raise ValueError
            self.saldo -= valor

        def transferir(self, conta_destino, valor):
            try:
                self.sacar(valor)
                conta_destino.depositar(valor)
            except ValueError:
                raise ValueError


class ContaCorrente(Conta):
    def __init__(self, titular, agencia, conta, saldo, limite):
        super().__init__(self, titular, agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if(valor > 0 and valor <= (self.saldo + self.limite)):
            raise ValueError
        self.saldo -= valor


class ContaPoupanca(Conta):
    def __init__(self, titular, agencia, conta, saldo):
        super().__init__(self, titular, agencia, conta, saldo)

    def calcular_rendimento(self, taxa):
        self.saldo += self.saldo * taxa / 100
