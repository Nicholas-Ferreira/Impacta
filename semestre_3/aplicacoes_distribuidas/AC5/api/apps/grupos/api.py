from flask import Blueprint, request, jsonify
from constants import API_URL
import requests as req

bp = Blueprint('grupos', __name__)

@bp.route('', methods=['GET'])
def index():
  grupos = req.get(f'{API_URL}/grupos').json()
  return jsonify(grupos), 200

@bp.route('/<int:id>', methods=['GET'])
def show(id):
  return {}, 200

@bp.route('/<int:id>', methods=['PATCH'])
def update(id):
  return {}, 200