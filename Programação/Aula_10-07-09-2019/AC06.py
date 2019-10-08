

class Funcionario:
    def __init__(self, codigo, nome, email, telefone, cpf):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf


class Coordenador(Funcionario):
    __cursos = []

    def __init__(self, codigo, nome, email, telefone, cpf, cursos):
        super().__init__(codigo, nome, email, telefone, cpf)
        self.__cursos = cursos

    def incluir_curso(self, curso):
        self.__cursos.append(curso)

    def get_cursos(self):
        return self.__cursos


class Professor(Funcionario):
    __disciplinas = []

    def __init__(self, codigo, nome, email, telefone, cpf, titulacao, area, disciplinas):
        super().__init__(codigo, nome, email, telefone, cpf)
        self.titulacao = titulacao
        self.area = area
        self.__disciplinas = disciplinas

    def incluir_disciplina(self, disciplina):
        soma = disciplina.carga_horaria
        for disciplina in self.__disciplinas:
            soma += disciplina.carga_horaria
        if soma > 200:
            raise ValueError
        else:
            self.__disciplinas.append(disciplina)

    def get_disciplinas(self):
        return self.__disciplinas


class Curso:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Disciplina:
    def __init__(self, codigo, nome, carga_horaria, curso):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.curso = curso


class Aluno:
    __disciplinas = []

    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.__disciplinas = disciplinas

    def incluir_disciplina(self, disciplina):
        if(len(self.__disciplinas) > 5):
            raise ValueError
        else:
            self.__disciplinas.append(disciplina)

    def get_disciplinas(self):
        return self.__disciplinas
