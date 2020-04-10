from flask import Blueprint, request, jsonify
from apps.alunos.models import Aluno

alunos = [
  Aluno(1, 'Nicholas'),
  Aluno(2, 'Wyuror'),
  Aluno(3, 'Falfume'),
  Aluno(4, 'Gilbyoun'),
  Aluno(5, 'Bazuko'),
  Aluno(6, 'Tuyguri'),
  Aluno(7, 'Xiafi')
]

bp = Blueprint('alunos', __name__)

def findById(_id):
  for aluno in alunos:
    if aluno.id == _id:
      return aluno
  return False

@bp.route('', methods=['GET'])
def index():
  return jsonify([a.to_dict() for a in alunos]), 200

@bp.route('/<int:id_aluno>', methods=['GET'])
def show(id_aluno):
  aluno = findById(id_aluno)
  if not aluno:
    return {}, 404
  return aluno.to_dict(), 200

@bp.route('', methods=['POST'])
def store():
  req = request.json
  if not req:
    return {'erro': 'Necessário envio do corpo'}, 400
  if 'nome' not in req:
    return {'erro': 'Aluno sem nome'}, 400
  if 'id' not in req:
    return {'erro': 'Aluno sem id'}, 400
  
  if findById(req['id']):
    return {'erro': 'ID ja utilizado'}, 400

  _aluno = Aluno(req['id'], req['nome'])
  alunos.append(_aluno)

  return _aluno.to_dict(), 200

@bp.route('/<int:id_aluno>', methods=['DELETE'])
def destroy(id_aluno):
  for idx, aluno in enumerate(alunos):
    if aluno.id == id_aluno:
      del alunos[idx]
      return {'msg': aluno.nome+' excluido'}, 200
  return {'erro': 'ID não encontrado'}, 404

@bp.route('/<int:id_aluno>', methods=['PUT'])
def update(id_aluno):
  req = request.json
  aluno = findById(id_aluno)
  if not aluno:
    return {'erro': 'ID não encontrado'}, 404

  aluno.nome = req['nome']

  return {'erro': 'Aluno alterado'}, 200
