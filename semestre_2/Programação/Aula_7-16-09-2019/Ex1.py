class Funcionario():
    
    def __init__(self, matricula, nome, salario):
        self.__matricula = matricula
        self.__nome = nome
        self.__salario = salario

    def get_matricula(self):
        return self.__matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_salario(self):
        return self.__salario
    def set_salario(self, valor):
        self.__salario = valor
    
alunos = []

alunos.append(Funcionario('1900953', 'Nicholas Ferreira', 3000))
alunos.append(Funcionario('1900519', 'Fernando Franco', 9000))
alunos.append(Funcionario('1901008', 'Leonardo Ferreira', 1277))
alunos.append(Funcionario('0000000', 'Lucas Ano', 1400))

print(alunos)
    

