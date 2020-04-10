from flask import Flask, render_template
from apps.alunos.api import bp as bp_alunos
from apps.professores.api import bp as bp_professor

app = Flask('app')

@app.route('/')
def index():
  return 'ok'

app.register_blueprint(bp_alunos, url_prefix='/alunos')
app.register_blueprint(bp_professor, url_prefix='/professores')

app.run(host='0.0.0.0', port='8080', debug=True)