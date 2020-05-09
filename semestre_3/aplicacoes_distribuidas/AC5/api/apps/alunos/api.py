from flask import Blueprint, request, jsonify
from constants import API_URL
import requests as req

bp = Blueprint('alunos', __name__)

@bp.route('', methods=['GET'])
def index():
  alunos = req.get(f'{API_URL}/alunos').json()
  return jsonify(alunos), 200

@bp.route('/<int:ra>', methods=['GET'])
def show(ra):
  aluno = req.get(f'{API_URL}/alunos/{ra}').json()
  if not aluno:
    return {}, 404
  return jsonify(aluno), 200

@bp.route('', methods=['POST'])
def store():
  return {}, 200

@bp.route('/<int:id>', methods=['DELETE'])
def destroy(id):
  return {}, 404

@bp.route('/<int:id>', methods=['PUT'])
def update(id):
  return {}, 200