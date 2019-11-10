# Linguagem de Programação II
# AC09 SI2B - LMS
# alunos: Nicholas Ferreira RA 1900953
#         Lucas Eduardo Ano RA 1900675


from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from getpass import getpass


eng = create_engine(f"mssql+pymssql://salas\\1900675:{getpass()}@sql.salas.aulas/fit_alunos")
Base = declarative_base(eng)


class Usuario(Base):
    __tablename__ = 'Usuario'
    id_usuario = Column('idUsuario', Integer, autoincrement=True, primary_key=True)
    senha = Column('Senha', String(30))
    data_expiracao = Column('DtExpiracao', String(8))


class Aluno(Base):
    __tablename__ = 'Aluno'
    id_aluno = Column('idAluno', Integer, autoincrement=True, primary_key=True)
    nome = Column('Nome', String(100))
    email = Column('Email', String(50))
    celular = Column('Celular', String(14))
    ra = Column('RA', Integer)


class Professor(Base):
    __tablename__ = 'Professor'
    id_professor = Column('idProfessor', Integer, autoincrement=True, primary_key=True)
    id_usuario = Column('idUsuario', Integer)
    email = Column('Email', String(50))
    celular = Column('Celular', String(14))
    apelido = Column('Apelido', String(15))


class Coordenador(Base):
    __tablename__ = 'Coordenador'
    id_coordenador = Column('idCoordenador', Integer, autoincrement=True, primary_key=True)
    id_usuario = Column('idUsuario', Integer)
    nome = Column('Nome', String(30))
    email = Column('Email', String(50))
    celular = Column('Celular', String(14))


class Disciplina(Base):
    __tablename__ = 'Disciplina'
    id_disciplina = Column('idDisciplina', Integer, autoincrement=True, primary_key=True)
    nome = Column('Nome', String(30))
    plano_de_ensino = Column('PlanoDeEnsino', String(500))
    carga_horaria = Column('CargaHoraria', Integer)
    competencias = Column('Competencias', String(500))
    habilidades = Column('Habilidades', String(500))
    ementa = Column('Ementa', String(500))
    id_coordenador = Column('idCoordenador', Integer)
    conteudo_programatico = Column('ConteudoProgramatico', String(500))
    bibliografia_basica = Column('BibliografiaBasica', String(500))
    bibliografia_complementar = Column('BibliografiaComplementar', String(500))
    percentual_pratico = Column('PercentualPratico', Integer)
    percentual_teorico = Column('PercentualTeorico', Integer)


class Curso(Base):
    __tablename__ = 'Curso'
    id_curso = Column('idCurso', Integer, autoincrement=True, primary_key=True)
    nome = Column('Nome', String(50))


def lista_alunos():
    '''
    retorna uma lista com os nomes de todos os Alunos do banco.
    '''
    Session = sessionmaker(eng)
    ses = Session()

    alunos = ses.query(Aluno).all()
    nome_alunos = []
    for i in alunos:
        nome_alunos.append(i.nome)

    return nome_alunos


def lista_cursos():
    '''
    retorna uma lista com os nomes de todos os Cursos do banco.
    '''
    Session = sessionmaker(eng)
    ses = Session()

    cursos = ses.query(Curso).all()
    nome_cursos = []
    for i in cursos:
        nome_cursos.append(i.nome)

    return nome_cursos


def lista_professores():
    '''
    retorna uma lista com os apelidos de todos os professores do banco.
    '''
    Session = sessionmaker(eng)
    ses = Session()

    professores = ses.query(Professor).all()
    apelido_professores = []
    for i in professores:
        apelido_professores.append(i.apelido)

    return apelido_professores


def lista_coordenadores():
    '''
    retorna uma lista com os nomes de todos os coordenadores do banco.
    '''
    Session = sessionmaker(eng)
    ses = Session()

    coordenadores = ses.query(Coordenador).all()
    nome_coordenadores = []
    for i in coordenadores:
        nome_coordenadores.append(i.nome)

    return nome_coordenadores


def lista_disciplinas():
    '''
    retorna uma lista com o nome de todas as Discplinas do banco.
    '''
    Session = sessionmaker(eng)
    ses = Session()

    discplinas = ses.query(Disciplina).all()
    nome_discplinas = []
    for i in discplinas:
        nome_discplinas.append(i.nome)

    return nome_discplinas


def carga_horaria_total():
    '''
    retorna a soma da carga horária de todas as diciplinas do banco
    '''
    Session = sessionmaker(eng)
    ses = Session()

    discplinas = ses.query(Disciplina).all()
    total = 0
    for i in discplinas:
        total += i.carga_horaria

    return total
