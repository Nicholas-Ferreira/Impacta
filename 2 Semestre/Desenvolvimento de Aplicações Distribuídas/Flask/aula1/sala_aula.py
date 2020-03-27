'''
 Nome: Nicholas Mota Ferreira
 RA: 1900953
'''

class Aluno():
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome


class Professor():
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome


database = {}
database["ALUNOS"] = []
database["PROFESSORES"] = []