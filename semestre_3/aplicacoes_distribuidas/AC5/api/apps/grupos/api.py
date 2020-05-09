from flask import Blueprint, request, jsonify

bp = Blueprint('grupos', __name__)

@bp.route('', methods=['GET'])
def index():
  grupos = []
  return {}, 200

@bp.route('/<int:id>', methods=['GET'])
def show(id):
  return {}, 200

@bp.route('', methods=['POST'])
def store():
  return {}, 200

@bp.route('/<int:id>', methods=['DELETE'])
def destroy(id):
  return {}, 404

@bp.route('/<int:id>', methods=['PUT'])
def update(id):
  return {}, 200