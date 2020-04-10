from flask import Flask, render_template
from apps.alunos.api import bp as bp_alunos
from apps.professores.api import bp as bp_professor
from apps.disciplinas.api import bp as bp_disciplina

app = Flask('app')

@app.route('/')
def index():
  return 'ok'

app.register_blueprint(bp_alunos, url_prefix='/alunos')
app.register_blueprint(bp_professor, url_prefix='/professores')
app.register_blueprint(bp_disciplina, url_prefix='/disciplinas')

app.run(host='0.0.0.0', port='8080', debug=True)