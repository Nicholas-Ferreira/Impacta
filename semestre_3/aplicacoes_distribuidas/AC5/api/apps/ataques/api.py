from flask import Blueprint, request, jsonify
from constants import API_URL
import requests as req

bp = Blueprint('ataques', __name__)

@bp.route('', methods=['GET'])
def index():
  ataques = req.get(f'{API_URL}/ataques').json()
  return jsonify(ataques), 200

@bp.route('/<int:codigo>', methods=['GET'])
def show(codigo):
  aluno = req.get(f'{API_URL}/ataques/{codigo}').json()
  if not aluno:
    return {}, 404
  return jsonify(aluno), 200

@bp.route('/<int:codigo>', methods=['PATCH'])
def update(codigo):
  req = request.json()
  ataques = req.patch(f'{API_URL}/ataques/{codigo}', req).json()
  if not ataques:
    return {}, 404
  return jsonify(ataques), 200