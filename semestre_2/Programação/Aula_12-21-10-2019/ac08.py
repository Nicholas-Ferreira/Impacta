from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @abstractmethod
    def exibir_dados(self):
        pass


class Cadastro:
    pessoas = []

    def __init__(self):
        pass

    def cadastrar_pessoa(self, Pessoa):
        self.pessoas.append(Pessoa)

    def exibir_cadastro(self):
        pass


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Cliente(Pessoa):
    def __init__(self, nome, nascimento, codigo):
        super().__init__(nome, nascimento)
        self.codigo = codigo

    def exibir_dados(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, salario):
        super().__init__(nome, nascimento)
        self.salario = salario

    def exibir_dados(self):
        pass

    def calcular_imposto(self):
        return 0.05 * self.salario


class Gerente(Funcionario):
    def __init__(self, nome, nascimento, salario, setor):
        super().__init__(nome, nascimento,  salario)
        self.setor = setor

    def calcular_imposto(self):
        return 0.07 * self.salario

    def exibir_dados(self):
        pass
