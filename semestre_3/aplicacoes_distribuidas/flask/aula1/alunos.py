'''
 Nome: Nicholas Mota Ferreira
 RA: 1900953
'''

from flask import jsonify, request
import sala_aula as sala

def listar_alunos():
  return jsonify(sala.database['ALUNOS'])

def novo_alunos():
  aluno = request.json
  if 'nome' not in aluno:
    return {'erro': 'aluno sem nome'}, 400

  for al in sala.database['ALUNOS']:
    if al['id'] == aluno['id']:
      return {'erro': 'id ja utilizada'}, 400

  sala.database['ALUNOS'].append(aluno)
  return jsonify(aluno), 200

def recuperar_alunos(id_aluno):
  for al in sala.database['ALUNOS']:
    if al['id'] == id_aluno:
      return jsonify(al)
  return {'erro': 'aluno nao encontrado'}, 400

def deletar_alunos(id_aluno):
  for i, aluno in enumerate(sala.database['ALUNOS']):
    if aluno['id'] == id_aluno:
      sala.database['ALUNOS'].pop(i)
      return {}, 200
  return {'erro': 'aluno nao encontrado'}, 400

def alterar_alunos(id_aluno):
  aluno = request.json
  if 'nome' not in aluno:
    return {'erro': 'aluno sem nome'}, 400
  for i, al in enumerate(sala.database['ALUNOS']):
    if al['id'] == id_aluno:
      sala.database['ALUNOS'][i].update(aluno)
      return aluno, 200
  return {'erro': 'aluno nao encontrado'}, 400