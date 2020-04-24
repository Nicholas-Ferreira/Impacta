from connection import Database
class PessoasModel(Database):
  def __init__(self):
    super().__init__()
    self.ddl()

  def ddl(self):
    tb_pessoas = """
    CREATE TABLE IF NOT EXISTS Pessoa (
      id INTEGER PRIMARY KEY autoincrement,
      nome TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    )
    """
    self.exec(tb_pessoas)
    print('Tabela criado com sucesso')

  def listar(self):
    sql = """
    SELECT * FROM Pessoa
    """
    return self.select(sql)

  def get(self, id):
    sql = """
    SELECT * FROM Pessoa WHERE id = :id
    """
    return self.select(sql, {"id": id})[0]
    
  def create(self, nome, email, id = None):
    sql = """
    INSERT INTO Pessoa(id, nome, email) VALUES (:id, :nome, :email)
    """
    dados = { "id": id, "nome": nome, "email": email }
    self.exec(sql, dados)
    print('Usuário criado')
    
  def update(self, id, nome, email):
    sql = """
    UPDATE Pessoa SET nome = :nome, email = :email WHERE id = :id
    """
    dados = { "id": id, "nome": nome, "email": email }
    self.exec(sql, dados)
    print('Usuário atualizado')

  def delete(self, id):
    sql = """
    DELETE FROM Pessoa WHERE id = :id
    """
    dados = { "id": id }
    self.exec(sql, dados)
    print('Usuário Deletado')
