from flask import Flask, jsonify, request
import sala_aula as sala
app = Flask('app')

@app.route('/')
def all():
  return sala.database

@app.route('/alunos', methods=['GET'])
def listar_alunos():
  return jsonify(sala.database['ALUNOS'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def recuperar_alunos(id_aluno):
  for al in sala.database['ALUNOS']:
    if al['id'] == id_aluno:
      return jsonify(al)
  return 'nao encontrado', 404

@app.route('/alunos', methods=['POST'])
def novo_alunos():
  aluno = request.json
  sala.database['ALUNOS'].append(aluno)
  return jsonify(aluno)

@app.route('/professores')
def listar_professores():
  return jsonify(sala.database['PROFESSORES'])

if __name__ == '__main__':
  app.run(host='localhost', port=8000, debug=True)