from flask import Blueprint, request, jsonify
from apps.professores.models import Professor

professores = [
  Professor(1, 'Lucas Mendes Marques Gonçalves'),
  Professor(2, 'Ericson de Souza Roza'),
  Professor(3, 'Osvaldo Kotaro Takai'),
  Professor(4, 'Emilio Murta Resende'),
  Professor(5, 'Leonardo Massayuki Takuno'),
  Professor(6, 'Lívia Rosa de Carvalho Sousa')
]

bp = Blueprint('professores', __name__)

def findById(_id):
  for professor in professores:
    if professor.id == _id:
      return professor
  return False

@bp.route('', methods=['GET'])
def index():
  return jsonify([p.to_dict() for p in professores]), 200

@bp.route('/<int:id_professor>', methods=['GET'])
def show(id_professor):
  professor = findById(id_professor)
  if not professor:
    return {}, 404
  return professor.to_dict(), 200

@bp.route('', methods=['POST'])
def store():
  req = request.json
  if not req:
    return {'erro': 'Necessário envio do corpo'}, 400
  if 'nome' not in req:
    return {'erro': 'Professor sem nome'}, 400
  if 'id' not in req:
    return {'erro': 'Professor sem id'}, 400
  
  if findById(req['id']):
    return {'erro': 'ID ja utilizado'}, 400

  _professor = Professor(req['id'], req['nome'])
  professores.append(_professor)
  return _professor.to_dict(), 200

@bp.route('/<int:id_professor>', methods=['DELETE'])
def destroy(id_professor):
  # Não deixe excluir o professor que seja coordenador de alguma disciplina.
  for idx, professor in enumerate(professores):
    if professor.id == id_professor:
      del professores[idx]
      return {'msg': professor.nome+' foi demitido'}, 200
  return {'erro': 'ID não encontrado'}, 404

@bp.route('/<int:id_professor>', methods=['PUT'])
def update(id_professor):
  req = request.json
  professor = findById(id_professor)
  if not professor:
    return {'erro': 'ID não encontrado'}, 404

  professor.nome = req['nome']

  return {'msg': 'Professor alterado'}, 200
