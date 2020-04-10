class Professor():
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
    
  def to_dict(self):
    disc = { 
      'id': self.id, 
      'nome': self.nome 
    }
    return disc
