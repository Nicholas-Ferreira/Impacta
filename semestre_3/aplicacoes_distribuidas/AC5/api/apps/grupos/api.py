from flask import Blueprint, request, jsonify
from constants import API_URL
import requests as req

bp = Blueprint('grupos', __name__)

@bp.route('', methods=['GET'])
def index():
  grupos = req.get(f'{API_URL}/grupos').json()
  if not grupos:
    return jsonify(grupos), 200
  return {}, 404

@bp.route('/<int:id>', methods=['GET'])
def show(id):
  grupo = req.get(f'{API_URL}/grupos/{id}').json()
  if not grupo:
    return jsonify(grupo), 200
  return {}, 404
