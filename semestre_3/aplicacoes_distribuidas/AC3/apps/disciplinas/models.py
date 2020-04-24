class Disciplina():
  def __init__(self, id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    self.id = id
    self.nome = nome
    self.status = status
    self.plano_ensino = plano_ensino
    self.carga_horaria = carga_horaria
    self.id_coordenador = id_coordenador
    
  def to_dict(self):
    disc = { 
      'id': self.id, 
      'nome': self.nome,
      'status': self.status,
      'plano_ensino': self.plano_ensino,
      'carga_horaria': self.carga_horaria,
      'id_coordenador': self.id_coordenador
    }
    return disc
