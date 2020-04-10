from flask import Blueprint, request, jsonify
from apps.disciplinas.models import Disciplina

disciplinas = [
  Disciplina(1, 'Estrutura de Dados', 1, '', 120, 1),
  Disciplina(2, 'Engenharia de Requisitos', 1, '', 120, 1),
  Disciplina(3, 'Oficina de Projeto de Empresa 1', 1, '', 120, 1),
  Disciplina(4, 'Desenvolvimento de Aplicações Distribuídas', 1, '', 120, 1),
  Disciplina(5, 'Análise e Modelagem de Sistemas', 1, '', 120, 1),
  Disciplina(6, 'Interface Homem Computador', 1, '', 120, 1),
]

bp = Blueprint('disciplinas', __name__)

def findById(_id):
  for disciplina in disciplinas:
    if disciplina.id == _id:
      return disciplina
  return False

@bp.route('', methods=['GET'])
def index():
  return jsonify([d.to_dict() for d in disciplinas]), 200

@bp.route('/<int:id_disciplina>', methods=['GET'])
def show(id_disciplina):
  disciplina = findById(id_disciplina)
  if not disciplina:
    return {}, 404
  return disciplina.to_dict(), 200

@bp.route('', methods=['POST'])
def store():
  from apps.professores.api import show as get_professores
  req = request.json
  if not req:
    return {'erro': 'Necessário envio do corpo'}, 400
  if 'id' not in req:
    return {'erro': 'Disciplina sem id'}, 400
  if 'nome' not in req:
    return {'erro': 'Disciplina sem nome'}, 400
  if 'status' not in req:
    return {'erro': 'Disciplina sem status'}, 400
  if 'plano_ensino' not in req:
    return {'erro': 'Disciplina sem plano de ensino'}, 400
  if 'carga_horaria' not in req:
    return {'erro': 'Disciplina sem carga horaria'}, 400
  if 'id_coordenador' not in req:
    return {'erro': 'Disciplina sem coordenador'}, 400
  
  if findById(req['id']):
    return {'erro': 'ID ja utilizado'}, 400

  professor = get_professores(req['id_coordenador'])
  if professor[1] != 200:
    return {'erro': 'Coordenador inexistente'}, 404

  _disciplina = Disciplina(**req)
  disciplinas.append(_disciplina)

  return _disciplina.to_dict(), 200

@bp.route('/<int:id_disciplina>', methods=['DELETE'])
def destroy(id_disciplina):
  for idx, disciplina in enumerate(disciplinas):
    if disciplina.id == id_disciplina:
      del disciplinas[idx]
      return {'msg': 'Disciplina '+disciplina.nome+' foi excluida'}, 200
  return {'erro': 'ID não encontrado'}, 404

@bp.route('/<int:id_disciplina>', methods=['PUT'])
def update(id_disciplina):
  from apps.professores.api import show as get_professores
  req = request.json
  disciplina = findById(id_disciplina)
  if not disciplina:
    return {'erro': 'ID não encontrado'}, 404
  if not req:
    return {'erro': 'Necessário envio do corpo'}, 400
  if 'nome' not in req:
    return {'erro': 'Disciplina sem nome'}, 400
  if 'status' not in req:
    return {'erro': 'Disciplina sem status'}, 400
  if 'plano_ensino' not in req:
    return {'erro': 'Disciplina sem plano de ensino'}, 400
  if 'carga_horaria' not in req:
    return {'erro': 'Disciplina sem carga horaria'}, 400
  if 'id_coordenador' not in req:
    return {'erro': 'Disciplina sem coordenador'}, 400

  professor = get_professores(req['id_coordenador'])
  if professor[1] != 200:
    return {'erro': 'Coordenador inexistente'}, 404

  disciplina.nome = req['nome']
  disciplina.status = req['status']
  disciplina.plano_ensino = req['plano_ensino']
  disciplina.carga_horaria = req['carga_horaria']
  disciplina.id_coordenador = req['id_coordenador']

  return {'msg': 'disciplina alterada'}, 200
