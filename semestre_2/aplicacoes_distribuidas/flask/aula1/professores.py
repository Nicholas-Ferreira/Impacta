'''
 Nome: Nicholas Mota Ferreira
 RA: 1900953
'''

from flask import jsonify, request
import sala_aula as sala

def listar_professores():
  return jsonify(sala.database['PROFESSORES'])

def novo_professores():
  professor = request.json
  if 'nome' not in professor:
    return {'erro': 'professor sem nome'}, 400

  for al in sala.database['PROFESSORES']:
    if al['id'] == professor['id']:
      return {'erro': 'id ja utilizada'}, 400

  sala.database['PROFESSORES'].append(professor)
  return jsonify(professor), 200

def recuperar_professores(id_professor):
  for al in sala.database['PROFESSORES']:
    if al['id'] == id_professor:
      return jsonify(al)
  return {'erro': 'professor nao encontrado'}, 400

def deletar_professores(id_professor):
  for i, professor in enumerate(sala.database['PROFESSORES']):
    if professor['id'] == id_professor:
      sala.database['PROFESSORES'].pop(i)
      return {}, 200
  return {'erro': 'professor nao encontrado'}, 400

def alterar_professores(id_professor):
  professor = request.json
  if 'nome' not in professor:
    return {'erro': 'professor sem nome'}, 400
  for i, al in enumerate(sala.database['PROFESSORES']):
    if al['id'] == id_professor:
      sala.database['PROFESSORES'][i].update(professor)
      return professor, 200
  return {'erro': 'professor nao encontrado'}, 400