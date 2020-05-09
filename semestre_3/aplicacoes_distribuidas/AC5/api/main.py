from flask import Flask, request, render_template

from apps.grupos.api import bp as bp_grupos
from apps.alunos.api import bp as bp_alunos

app = Flask('app')

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')
  
app.register_blueprint(bp_grupos, url_prefix='/grupos')
app.register_blueprint(bp_alunos, url_prefix='/alunos')

app.run(host='0.0.0.0', port='8081', debug=True)