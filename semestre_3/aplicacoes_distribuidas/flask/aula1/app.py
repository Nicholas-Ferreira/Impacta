'''
 Nome: Nicholas Mota Ferreira
 RA: 1900953
'''

from flask import Flask, jsonify, request
import sala_aula as sala
import alunos
import professores

app = Flask('app')

@app.route('/')
def all():
  return sala.database

@app.route('/reseta', methods=['POST'])
def resetar():
  sala.database['ALUNOS'] = []
  sala.database['PROFESSORES'] = []
  return {}, 200

### Rotas Alunos ###
@app.route('/alunos', methods=['GET'])
def listar_alunos():
  return alunos.listar_alunos()

@app.route('/alunos', methods=['POST'])
def novo_alunos():
  return alunos.novo_alunos()

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def recuperar_alunos(id_aluno):
  return alunos.recuperar_alunos(id_aluno)

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deletar_alunos(id_aluno):
  return alunos.deletar_alunos(id_aluno)

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def alterar_alunos(id_aluno):
  return alunos.alterar_alunos(id_aluno)

### Rotas Professores ###
@app.route('/professores')
def listar_professores():
  return professores.listar_professores()

@app.route('/professores', methods=['POST'])
def novo_professores():
  return professores.novo_professores()

@app.route('/professores/<int:id_professor>', methods=['GET'])
def recuperar_professores(id_professor):
  return professores.recuperar_professores(id_professor)

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deletar_professores(id_professor):
  return professores.deletar_professores(id_professor)

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def alterar_professores(id_professor):
  return professores.alterar_professores(id_professor)

if __name__ == '__main__':
  app.run(host='localhost', port=5002, debug=True)