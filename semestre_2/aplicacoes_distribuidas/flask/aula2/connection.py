import sqlite3

class Database:
  def __init__(self):
    print('Banco de Dados conectado!')

  def exec(self, sql, dados = {}):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    cursor.close()
    connection.close()

  def select(self, sql, dados = {}):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    lista = cursor.fetchall()
    cursor.close()
    connection.close()
    return lista